BASEDIR=$(dirname "$0")
home_dir="$BASEDIR"
run_dir="$home_dir/run"
sh ${run_dir}/khi/plot_khi.sh
for res in 128 256 512; do
    rotor_dir="${run_dir}/rotor"
    pvpython ${rotor_dir}/state.py --input ${res}
done
pvpython ${run_dir}/shock_diffraction/density.py
pvpython ${run_dir}/shock_diffraction/mach.py

pvpython ${run_dir}/ssw_roll_2d/state_roll.py

tang_dir="${run_dir}/tang"
pvpython ${tang_dir}/extract_cuts.py
julia --project=$home_dir ${tang_dir}/plot_lines.jl
cp ${tang_dir}/*pdf .

pvpython ${tang_dir}/plot_tang.py
pvpython ${tang_dir}/plot_tang_pressure.py

tmp_dir="${run_dir}/tenmom_super_stiff_2d"
for file in ${tmp_dir}/*.py; do
    pvpython "$file"
done

final_files="state_rho_final.py state_vx_final.py state_vy_final.py state_det.py"
for file in $final_files; do
    pvpython "${tmp_dir}/$file" --nx 400
done
