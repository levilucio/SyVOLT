#! /bin/sh

#echo "Testing test_atlTrans.py" > results_ATL.txt
#for i in {1..5}
#do
#        echo -e "\nATL Run: $i"
#        /usr/bin/time python3 test_atlTrans.py --no_svg 2>&1 | tail -15 >> results_ATL.txt
#done

echo "Testing test_atlTrans_extended.py" > results_ATL_extended.txt
for i in {1..5}
do
        echo -e "\nATL Extended Run: $i"
        /usr/bin/time python3 test_atlTrans_extended.py --no_svg 2>&1 | tail -15 >> results_ATL_extended.txt
done


