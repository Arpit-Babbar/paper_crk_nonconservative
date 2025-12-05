using TrixiBase: trixi_include

epsilon_relaxation_array = (1e-1, 1e-2, 1e-3, 1e-4, 1e-12)
eps2string = Dict(1e-1 => "1", 1e-2 => "2", 1e-3 => "3", 1e-4 => "4", 1e-12 => "12")
for i in 1:5
    epsilon_relaxation = epsilon_relaxation_array[i]
    trixi_include(joinpath(@__DIR__, "run_jin_xin_burg1d.jl"), epsilon_relaxation = epsilon_relaxation,
                  degree = 3, solver = cSSP2IMEX433(), nx = 20,
                  saveto = joinpath(@__DIR__, "jin_xin_nx20_eps$(eps2string[epsilon_relaxation])"))
end
