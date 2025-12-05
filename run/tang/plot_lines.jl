using CSV
# using Plots
using PyPlot
using Tenkai: utils_dir

include("$utils_dir/plot_python_solns.jl")
# plotlyjs()

# plot()

# plt.figure(grid = true)
fig, ax = plt.subplots()
ax.grid(true, linestyle = "--")
ax.set_xlabel("\$x\$")
ax.set_ylabel("\$p\$")

ref_data_3125 = CSV.File(joinpath(@__DIR__, "ref_data_tang", "orszag_tang_athena_0_3125.csv"))
ref_data_3125_x = ref_data_3125.x
ref_data_3125_rho = ref_data_3125.p
ax.scatter(ref_data_3125_x, ref_data_3125_rho, label = "Athena", color = "red")

data_3125 = CSV.File(joinpath(@__DIR__, "pressure_profile_3125.csv"))
data_3125_x = data_3125.var"Points:0"
data_3125_p = data_3125.p
ax.plot(data_3125_x, data_3125_p, label = "cRKFR")

ax.legend()

plt.show()
plt
fig.savefig(joinpath(@__DIR__, "tang_line_cut_0_3125.pdf"))

fig

fig, ax = plt.subplots()
ax.grid(true, linestyle = "--")
ax.set_xlabel("\$x\$")
ax.set_ylabel("\$p\$")

ref_data_4277 = CSV.File(joinpath(@__DIR__, "ref_data_tang", "orszag_tang_athena_0_4277.csv"))
ref_data_4277_x = ref_data_4277.x
ref_data_4277_rho = ref_data_4277.p
ax.scatter(ref_data_4277_x, ref_data_4277_rho, label = "Athena", color = "red")

data_4277 = CSV.File(joinpath(@__DIR__, "pressure_profile_4277.csv"))
data_4277_x = data_4277.var"Points:0"
data_4277_p = data_4277.p
ax.plot(data_4277_x, data_4277_p, label = "cRKFR")

ax.legend()

plt.show()
plt
fig.savefig(joinpath(@__DIR__, "tang_line_cut_0_4277.pdf"))

fig