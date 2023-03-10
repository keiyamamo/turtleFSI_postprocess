#!/bin/bash

# This script is used to test the python script that accepts an argument and
# save the output to a file. Here, we are testing the script by passing a
# argument inside the for loop and see if we get output for each iteration.

for i in {1..3}
do
    python save_pickle.py -nx $i
done
