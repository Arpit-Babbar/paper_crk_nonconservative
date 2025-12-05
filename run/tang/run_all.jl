using TrixiBase: trixi_include

trixi_include(joinpath(@__DIR__, "run_mhd_tang.jl"), solver = TrixiRKSolver(),
              solution_points = "gll", correction_function = "g2",
              nx = 128, ny = 128, degree = 3,
              saveto = joinpath(@__DIR__, "trixi_3"))

trixi_include(joinpath(@__DIR__, "run_mhd_tang.jl"), solver = cRK44(),
              nx = 128, ny = 128, degree = 3,
              saveto = joinpath(@__DIR__, "crk44_3"))

trixi_include(joinpath(@__DIR__, "run_mhd_tang.jl"), solver = TrixiRKSolver(),
              solution_points = "gll", correction_function = "g2",
              nx = 128, ny = 128, degree = 4,
              saveto = joinpath(@__DIR__, "trixi_4"))

trixi_include(joinpath(@__DIR__, "run_mhd_tang.jl"), solver = cRK44(),
              nx = 128, ny = 128, degree = 4,
              saveto = joinpath(@__DIR__, "crk44_4"))

trixi_include(joinpath(@__DIR__, "elixir_mhd_tang.jl"))

