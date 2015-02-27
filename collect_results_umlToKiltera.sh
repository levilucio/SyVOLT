#! /bin/sh

echo "Testing test_umlToKiltera.py" > results_umlToKiltera.txt
for i in {1..2}
do
   echo -e "\nNumber of rules: $i" >> results_umlToKiltera.txt
   /usr/bin/time python2 test_umlToKiltera.py --no_svg --num_rules=$i  2>&1 | tail -4 >> results_umlToKiltera.txt
done
