echo "Testing test_GM2Autosar_transformation.py" > results_GM.txt
#for j in {1..8}
#do
#        for i in {1..5}
#        do
#                echo -e "\nGM Contract Num: $j Run: $i"
#                echo -e "\nGM Contract Num: $j Run: $i" >> results_GM.txt
#                /usr/bin/time python3 test_GM2Autosar_transformation.py --no_svg --skip_tests --contract=$j 2>&1 | tail -10 >> results_GM.txt
#        done
#        
#        for i in {1..5}
#        do
#                echo -e "\nGM Handbuilt Contract Num: $j Run: $i Handbuilt"
#                echo -e "\nGM Handbuilt Contract Num: $j Run: $i Handbuilt" >> results_GM.txt
#                /usr/bin/time python3 test_GM2Autosar_transformation.py --no_svg --skip_tests --contract=$j --handbuilt 2>&1 | tail -10 >> results_GM.txt
#        done
#done

for i in {1..5}
do
        echo -e "\nGM Run: $i Handbuilt"
        echo -e "\nGM Run: $i Handbuilt" >> results_GM.txt
        /usr/bin/time python3 test_GM2Autosar_transformation.py --no_svg --skip_tests --handbuilt 2>&1 | tail -10 >> results_GM.txt
done

for i in {1..5}
do
        echo -e "\nGM Run: $i"
        echo -e "\nGM Run: $i" >> results_GM.txt
        /usr/bin/time python3 test_GM2Autosar_transformation.py --no_svg --skip_tests 2>&1 | tail -10 >> results_GM.txt
done
