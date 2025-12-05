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
    err_time = to.time(sol["aux"].timer["Compute error"])
    @show full_time, write_time, err_time
    return (full_time - write_time - err_time) * 1e-9
end

run_file = joinpath(@__DIR__, "run_mhd_alfven_wave.jl")

final_time_global = 2.0
nx_array = [16, 32, 64, 128]
nx_length = length(nx_array)
arrays_gl = Vector([zeros(nx_length, 3) for _ in 1:3])
arrays_gll = Vector([zeros(nx_length, 3) for _ in 1:3])

degree2crk = Dict(1 => cRK22(), 2 => cRK33(), 3 => cRK44())

# GL, radau
for (i, nx) in enumerate(nx_array)
    for degree in 1:3
        trixi_include(run_file, solver = degree2crk[degree],
                      degree = degree, final_time = 1e-6, nx = nx, ny = nx)
        sol_crk = trixi_include(run_file, solver = degree2crk[degree],
                                degree = degree, final_time = final_time_global, nx = nx,
                                ny = nx, solution_points = "gl",
                                correction_function = "radau",
                                limiter = setup_limiter_none())
        error_crk = sol_error(sol_crk)
        time_crk = sol_time(sol_crk)
        arrays_gl[degree][i, 1:3] .= nx, error_crk, time_crk
    end
end

mkpath(joinpath(@__DIR__, "results"))
for degree in 1:3
    writedlm(joinpath(@__DIR__, "results", "alfven_gl$(degree).txt"), arrays_gl[degree])
end

# gll, g2
for (i, nx) in enumerate(nx_array)
    for degree in 1:3
        trixi_include(run_file, solver = degree2crk[degree],
                      degree = degree, final_time = 1e-6, nx = nx, ny = nx)
        sol_gll = trixi_include(run_file, solver = degree2crk[degree],
                                 degree = degree, final_time = final_time_global, nx = nx,
                                 ny = nx, solution_points = "gll",
                                 correction_function = "g2",
                                 limiter = setup_limiter_none())
        error_gll = sol_error(sol_gll)
        time_gll = sol_time(sol_gll)
        arrays_gll[degree][i, 1:3] .= nx, error_gll, time_gll
    end
end

for degree in 1:3
    writedlm(joinpath(@__DIR__, "results", "alfven_gll$(degree).txt"), arrays_gll[degree])
end