#! /bin/sh

echo "Testing test_mbeddr.py" > results.txt
for i in {1..15}
do
   echo -e "\nNumber of rules: $i" >> results.txt
   /usr/bin/time python2 test_mbeddr.py --no_svg --num_rules=$i  2>&1 | tail -4 >> results.txt
done
