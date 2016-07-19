#! /bin/sh

echo "Testing test_slicing.py" > results_slicing2.txt

for j in {0..15}
do
   for i in {0..2}
   do
        echo -e "\nUML to Kiltera Run: $i $j"
      /usr/bin/time python3 test_umlToKiltera.py --no_svg --slice=$j 2>&1 | tail -10 >> results_slicing2.txt
   done
done
