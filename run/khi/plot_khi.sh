BASEDIR=$(dirname "$0")
for no in 025 040 050 060 070 080 090 100; do
	pvpython "$BASEDIR/state.py" --input_no ${no}
done	
