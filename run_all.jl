import Pkg
Pkg.activate(@__DIR__)
Pkg.instantiate()
using TrixiBase: trixi_include

run_dir = joinpath(@__DIR__, "run")
include(joinpath(run_dir, "burg_stiff", "generate_burg_stiff.jl"))
include(joinpath(run_dir, "convergence_alfven_wave", "convergence.jl"))
include(joinpath(run_dir, "convergence_multiion", "convergence.jl"))
include(joinpath(run_dir, "jin_xin", "generate_jin_xin.jl"))
include(joinpath(run_dir, "khi", "run_multiion_khi.jl"))
include(joinpath(run_dir, "reactive_rp", "run_all_reactive.jl"))
include(joinpath(run_dir, "rotor", "run_all.jl"))
include(joinpath(run_dir, "shock_diffraction", "run_reactive_euler_shock_diffraction.jl"))
include(joinpath(run_dir, "ssw_roll_1d", "run_ssw_roll_1.jl"))
include(joinpath(run_dir, "ssw_roll_1d", "run_ssw_roll_2.jl"))
include(joinpath(run_dir, "ssw_roll_2d", "run_ssw_roll_wave.jl"))
include(joinpath(run_dir, "sup_burg_stiff", "generate_all_sup_burg.jl"))
include(joinpath(run_dir, "tang", "run_mhd_tang.jl"))
include(joinpath(run_dir, "tenmom_super_stiff_1d", "generate_tmp_super_stiff.jl"))

for nx in (50, 400)
    trixi_include(joinpath(run_dir, "tenmom_super_stiff_2d", "run_tenmom_two_rare_source_super_stiff.jl"), nx = nx, ny = nx)
end

include(joinpath(run_dir, "varadv", "run_noncons_varadv.jl"))
include(joinpath(run_dir, "varadv", "convergence.jl"))
