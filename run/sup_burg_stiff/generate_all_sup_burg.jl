using Tenkai.Trixi: trixi_include

outdir = joinpath(@__DIR__, "burg_stiff_shock_1d_coarse_crk_imex433")
trixi_include(joinpath(@__DIR__, "run_shock_1_coarse.jl"), solver_single = cSSP2IMEX433(),
              saveto = outdir)

ua_homogeneous = sol["aux"].cache_homogeneous.ua
xc = sol["grid"].xc
writedlm(joinpath(outdir, "avg_homogeneous.txt"), hcat(xc, ua_homogeneous[1, 1:end-1]))

outdir = joinpath(@__DIR__, "burg_stiff_shock_1d_fine_crk_imex433")
trixi_include(joinpath(@__DIR__, "run_shock_1_fine.jl"), solver_single = cSSP2IMEX433(),
              saveto = outdir)

ua_homogeneous = sol["aux"].cache_homogeneous.ua
xc = sol["grid"].xc
writedlm(joinpath(outdir, "avg_homogeneous.txt"), hcat(xc, ua_homogeneous[1, 1:end-1]))
