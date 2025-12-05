using TrixiBase

a_arr = [0.12, 0.14, LinRange(0.2,1,9)...]
for a in a_arr
    try
      trixi_include(joinpath(@__DIR__, "run_multiion_khi.jl"), amax = a)
    catch e
    end
end
