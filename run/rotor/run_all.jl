using TrixiBase: trixi_include

for nx in (128, 256, 512)
    trixi_include(joinpath(@__DIR__, "run_mhd_rotor.jl"), nx = nx, ny = nx)
end
