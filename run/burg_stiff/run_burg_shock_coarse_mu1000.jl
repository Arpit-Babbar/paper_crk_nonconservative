using Tenkai.TenkaicRK
using Tenkai
using Tenkai.StaticArrays
using Tenkai.TenkaicRK: newton_solver
Eq = Tenkai.EqBurg1D
# Submodules

#------------------------------------------------------------------------------
xmin, xmax = -5.0, 5.0

boundary_condition = (dirichlet, neumann)
final_time = 5.0

function initial_value_jump(x)
    if x >= 0.0
        return 0.0
    else
        return 1.0
    end
end

function exact_solution_burg1d(x, t)
    if x - 0.5 * t >= 0.0
        return 0.0
    else
        return 1.0
    end
end
initial_value, exact_solution = initial_value_jump, exact_solution_burg1d

boundary_value = exact_solution

degree = 3
solver_single = cSSP2IMEX433()
solver = DoublecRKSourceSolver(solver_single)
solution_points = "gl"
correction_function = "radau"
numerical_flux = Eq.rusanov
bound_limit = "no"
bflux = extrapolate

nx_() = 20 # Kept small for CI
nx = nx_()
bounds = ([-Inf], [Inf])
cfl = 0.0
save_iter_interval = 0
save_time_interval = 0.0 * final_time
compute_error_interval = 1
animate_ = true
tvbM = 0.0

cfl_safety_factor_() = 0.9
cfl_safety_factor = cfl_safety_factor_()

dt() = cfl_safety_factor_() / ((degree + 1) * nx_())
mu() = 1000.0

struct SourceTermBurgNonLinear{RealT <: Real}
    mu::RealT
end

function (s::SourceTermBurgNonLinear)(u, x, t, eq)
    SVector(-s.mu * u[1] * (u[1] - 1.0) * (u[1] - 0.9))
end

source_terms = SourceTermBurgNonLinear(mu())

function TenkaicRK.get_cache_node_vars(aux, u1,
                                       problem::Problem{<:Real, <:SourceTermBurgNonLinear},
                                       scheme,
                                       eq, i, cell)
    (; cache_homogeneous) = aux
    u1 = cache_homogeneous.u1
    # u1 = aux.cache_source.u1
    u_node = get_node_vars(u1, eq, i, cell)
    return u_node
end

struct ImplicitSource{LHS,Source, X, Equations <: AbstractEquations, RealT <: Real}
    lhs::LHS
    source::Source
    coefficient::RealT
    x::X
    t::RealT
    equation::Equations
end

function (f::ImplicitSource)(u_new)
    u_new - f.lhs -
    f.coefficient * f.source(u_new, f.x, f.t, f.equation)
end

@noinline function TenkaicRK.implicit_source_solve(lhs, eq, x, t, coefficient,
                                         source_terms::SourceTermBurgNonLinear,
                                         u_node)
    if u_node[1] > 0.5 # The paper used 0.9
        initial_guess = SVector(1.0)
    else u_node[1] < 0.5
        initial_guess = SVector(0.0)
    end

    # implicit_F(u_new) = u_new - lhs -
    #                     coefficient * TenkaicRK.calc_source(u_new, x, t, source_terms, eq)
    implicit_F = ImplicitSource(lhs, source_terms, coefficient, x, t, eq)

    # tol = 10.0 / 110.0
    tol = 1.0 / nx_()
    maxiters = 1000000
    # if x < -0.1
    #     u_new = newton_solver(implicit_F, initial_guess, tol, maxiters)
    # else
    #     u_new = TenkaicRK.picard_solver(implicit_F, initial_guess, tol, maxiters, 0.0000001)
    # end

    # u_new = newton_solver(implicit_F, initial_guess, tol, maxiters)

    # Possibly incorrect solution, use a better iterative solver
    # if abs(u_new[1] - initial_guess[1]) > 0.5
        u_new = TenkaicRK.picard_solver(implicit_F, initial_guess, tol, maxiters, 0.0000001)
    # end

    # @assert maximum(implicit_F(u_new))<10 * tol implicit_F(u_new)
    s_new = TenkaicRK.calc_source(u_new, x, t, source_terms, eq)
    return u_new, s_new
end

#------------------------------------------------------------------------------
grid_size = nx
domain = [xmin, xmax]
problem = Problem(domain, initial_value, boundary_value,
                  boundary_condition, final_time, exact_solution,
                  source_terms = source_terms)
equation = Eq.get_equation()
limiter = setup_limiter_blend(blend_type = fo_blend_imex(equation),
                              #   indicating_variables = Eq.rho_p_indicator!,
                              indicating_variables = Eq.conservative_indicator!,
                              reconstruction_variables = conservative_reconstruction,
                              indicator_model = "gassner",
                              amax = 1.0,
                              pure_fv = false)
scheme = Scheme(solver, degree, solution_points, correction_function,
                numerical_flux, bound_limit, limiter, bflux)
param = Parameters(grid_size, cfl, bounds, save_iter_interval,
                   save_time_interval, compute_error_interval, animate = animate_,
                   cfl_safety_factor = cfl_safety_factor,
                   saveto = "none")
#------------------------------------------------------------------------------
sol = Tenkai.solve(equation, problem, scheme, param);

show(sol["errors"])

return sol;
p_ua = sol["plot_data"].p_ua

ua = sol["ua"]

u_homogeneous = sol["aux"].cache_homogeneous.ua
xc = sol["grid"].xc

using Plots
scatter(xc, u_homogeneous[1, 1:nx], label = "Homogeneous Solution", lw = 2, legend=:bottomleft)
scatter!(xc, ua[1, 1:nx], label = "CRK Solution", lw = 2)
exact_t = x -> exact_solution_burg1d(x, final_time)
plot!(xc, exact_t.(xc), label = "Exact Solution", lw = 2)
