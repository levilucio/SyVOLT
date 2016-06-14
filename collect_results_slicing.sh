#! /bin/sh

echo "Testing test_slicing.py" > results_slicing.txt

for i in {1..1}
do
   for j in {1..10}
   do
      /usr/bin/time python3 test_atlTrans_extended.py --no_svg --slice=$j 2>&1 | tail -10 >> results_slicing.txt
   done
done
