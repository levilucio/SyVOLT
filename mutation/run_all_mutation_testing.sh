#!/bin/bash

set -e

cd ..
mkdir -p results

declare -i loop_int
loop_int=2

run_test () {
  echo "$1" > timing.txt
  for (( i=0; i < $loop_int; i++ ))
  do
    /usr/bin/time python3 do_mutation_testing.py $1 $2 2>> timing.txt
    mv mutation_testing.xml results/$1$3_mutation_testing.xml
  done
  mv timing.txt results/$1$3_timing.txt
}


#True is integration tests, False is unit tests
#run_test "F2P" "True" ""
#run_test "F2P" "False" "unit"
#
#run_test "RSS" "False" "unit"
#
#run_test "UML2ER" "True" ""
#run_test "UML2ER" "False" "unit"

run_test "GM" "" ""
run_test "Kiltera" "" ""


