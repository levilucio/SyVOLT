#! /bin/sh

echo "Testing test_umlToKiltera.py" > results_umlToKiltera_sliced.txt
for j in {8..8}
do
        for i in {1..5}
        do
                echo -e "\nContract Num: $j Run: $i"
                echo -e "\nContract Num: $j Run: $i" >> results_umlToKiltera_sliced.txt
                /usr/bin/time python3 test_umlToKiltera.py --no_svg --skip_tests --slice=$j 2>&1 | tail -14 >> results_umlToKiltera_sliced.txt
        done
done


#echo "Testing test_umlToKiltera.py" > results_umlToKiltera.txt
#for j in {0..15}
#do
#        for i in {1..5}
#        do
#                echo -e "\nContract Num: $j Run: $i"
#                echo -e "\nContract Num: $j Run: $i" >> results_umlToKiltera.txt
#                /usr/bin/time python3 test_umlToKiltera.py --no_svg --skip_tests --contract=$j 2>&1 | tail -14 >> results_umlToKiltera.txt
#        done
#done





