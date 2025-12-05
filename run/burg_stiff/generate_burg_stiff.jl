using DelimitedFiles
using Tenkai.Trixi: trixi_include
using Tenkai.TenkaicRK

outdir = joinpath(@__DIR__, "burg_stiff_shock_coarse_crk_imex433")
trixi_include(joinpath(@__DIR__, "run_burg_shock_coarse.jl"), solver_single = cSSP2IMEX433(),
              saveto = outdir, final_time = 4.0)
ua_homogeneous = sol["aux"].cache_homogeneous.ua
xc = sol["grid"].xc
writedlm(joinpath(outdir, "avg_homogeneous.txt"), hcat(xc, ua_homogeneous[1, 1:end-1]))

outdir = joinpath(@__DIR__, "burg_stiff_shock_fine_crk_imex433")
trixi_include(joinpath(@__DIR__, "run_burg_shock_fine.jl"), solver_single = cSSP2IMEX433(),
              saveto = outdir, final_time = 4.0)
ua_homogeneous = sol["aux"].cache_homogeneous.ua
xc = sol["grid"].xc
writedlm(joinpath(outdir, "avg_homogeneous.txt"), hcat(xc, ua_homogeneous[1, 1:end-1]))

outdir = joinpath(@__DIR__, "burg_stiff_rare_coarse_crk_imex433")
trixi_include(joinpath(@__DIR__, "run_burg_rare_coarse.jl"), solver_single = cSSP2IMEX433(),
              saveto = outdir)
ua_homogeneous = sol["aux"].cache_homogeneous.ua
xc = sol["grid"].xc
writedlm(joinpath(outdir, "avg_homogeneous.txt"), hcat(xc, ua_homogeneous[1, 1:end-1]))

outdir = joinpath(@__DIR__, "burg_stiff_rare_fine_crk_imex433")
trixi_include(joinpath(@__DIR__, "run_burg_rare_fine.jl"), solver_single = cSSP2IMEX433(),
              saveto = outdir)
ua_homogeneous = sol["aux"].cache_homogeneous.ua
xc = sol["grid"].xc
writedlm(joinpath(outdir, "avg_homogeneous.txt"), hcat(xc, ua_homogeneous[1, 1:end-1]))
