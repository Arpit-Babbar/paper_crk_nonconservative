using Tenkai
using Tenkai.TenkaicRK
using TrixiBase: trixi_include

final_time = 1.0
Eq = Tenkai.TenkaicRK.EqEulerReactive1D

trixi_include(joinpath(@__DIR__, "run_reactive_rp1.jl"),
              solver = cSSP2IMEX433(),
              nx = 100, # 4000 / (degree + 1)
              cfl = 0.0,
              cfl_safety_factor = 0.9,
              save_iter_interval = 0,
              indicating_variables = Eq.rho_p_and_cons_indicator!,
              degree = 3,
              save_time_interval = 0.0 * final_time,
              pure_fv = false,
              debug_blend = false,
              indicator_model = "gassner",
              bound_limit = "no",
              A = 164180.0,
              saveto = joinpath(@__DIR__, "reactive_rp1_nx100"))

trixi_include(joinpath(@__DIR__, "run_reactive_rp1.jl"),
              solver = cSSP2IMEX433(),
              nx = 100, # 4000 / (degree + 1)
              cfl = 0.0,
              indicating_variables = Eq.rho_p_and_cons_indicator!,
              cfl_safety_factor = 2.0,
              save_iter_interval = 0,
              degree = 3,
              save_time_interval = 0.0 * final_time,
              pure_fv = false,
              debug_blend = false,
              indicator_model = "model1",
              bound_limit = "no",
              A = 164180.0,
              saveto = joinpath(@__DIR__, "reactive_rp1_nx100_cfl2"))

trixi_include(joinpath(@__DIR__, "run_reactive_rp1.jl"),
              solver = cSSP2IMEX433(),
              nx = 1000, # 4000 / (degree + 1)
              cfl = 0.0,
              cfl_safety_factor = 0.9,
              save_iter_interval = 0,
              degree = 3,
              indicating_variables = Eq.rho_p_and_cons_indicator!,
              save_time_interval = 0.0 * final_time,
              pure_fv = false,
              debug_blend = false,
              indicator_model = "gassner",
              bound_limit = "no",
              A = 164180.0,
              saveto = joinpath(@__DIR__, "reactive_rp1_nx1000"))

trixi_include(joinpath(@__DIR__, "run_reactive_rp1.jl"),
              solver = cIMEX111(),
              degree = 0,
              limiter = setup_limiter_none(),
              nx = 1000, # 4000 / (degree + 1)
              cfl = 0.0, cfl_safety_factor = 0.9,
              save_iter_interval = 0,
              save_time_interval = 0.0,
              pure_fv = false,
              A = 164180.0,
              bound_limit = "no",
              saveto = joinpath(@__DIR__, "reactive_rp1_deg0"))
