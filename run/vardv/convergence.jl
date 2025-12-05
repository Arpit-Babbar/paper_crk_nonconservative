using Tenkai
using Tenkai.TenkaicRK

using TrixiBase: trixi_include
using DelimitedFiles
import TimerOutputs as to

function sol_error(sol)
    return sol["errors"]["l2_error"]
end

function sol_time(sol)
    full_time = to.tottime(sol["aux"].timer)
    write_time = to.time(sol["aux"].timer["Write solution"])
    local err_time
    try
        err_time = to.time(sol["aux"].timer["Compute error"])
    catch _
        err_time = 0.0
    end
    @show full_time, write_time, err_time
    return (full_time - write_time - err_time) * 1e-9
end

run_file = joinpath(@__DIR__, "run_noncons_varadv.jl")

final_time_global = 1.0
nx_array = [8, 16, 32, 64]
nx_length = length(nx_array)
arrays_gl = Vector([zeros(nx_length, 3) for _ in 1:3])
array_gll = Vector([zeros(nx_length, 3) for _ in 1:3])

degree2crk = Dict(1 => cRK22(), 2 => cRK22(), 3 => cRK22())

for (i, nx) in enumerate(nx_array)
    cfl_arr = [1.0, 0.333, 0.170, 0.103, 0.069, 0.02419]
    for degree in 1:3
        # trixi_include(run_file, solver = degree2crk[degree],
        #               degree = degree, final_time = 1e-6, nx = nx)
        cfl = 0.1 * cfl_arr[degree + 1] # Variable advection equations require smaller time steps
        sol_gl = trixi_include(run_file, solver = degree2crk[degree],
                                degree = degree, final_time = final_time_global, nx = nx,
                                solution_points = "gl",
                                correction_function = "radau",
                                limiter = setup_limiter_none(),
                                cfl = cfl)
        sol_gll = trixi_include(run_file, solver = degree2crk[degree],
                                degree = degree, final_time = final_time_global, nx = nx,
                                solution_points = "gll",
                                correction_function = "g2",
                                limiter = setup_limiter_none(),
                                cfl = cfl)
        error_gl = sol_error(sol_gl)
        time_gl = sol_time(sol_gl)
        arrays_gl[degree][i, 1:3] .= nx, error_gl, time_gl
        error_gll = sol_error(sol_gll)
        time_gll = sol_time(sol_gll)
        array_gll[degree][i, 1:3] .= nx, error_gll, time_gll
    end
end

mkpath(joinpath(@__DIR__, "results"))
for degree in 1:3
    writedlm(joinpath(@__DIR__, "results", "varadv_gl$(degree).txt"),
             arrays_gl[degree])
    writedlm(joinpath(@__DIR__, "results", "varadv_gll$(degree).txt"),
             array_gll[degree])
end
