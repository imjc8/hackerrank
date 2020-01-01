#!/bin/python3
# 01/01/2020
# https://www.hackerrank.com/challenges/between-two-sets/problem


import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

from functools import reduce

def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
 
    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    count = sum([1 for x in range(max_lcm, min_gcd+1, max_lcm) if min_gcd % x == 0])
 
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #user inputs, space-separated, number of elements in array a and v
    first_multiple_input = input().rstrip().split()
    #assign values from user input above
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    #user input, space-separated, for array 'arr'
    arr = list(map(int, input().rstrip().split()))
    #user input, space-separated, for array 'brr'
    brr = list(map(int, input().rstrip().split()))

    #function call
    total = getTotalX(arr, brr)

    #print and write to file
    print(total)
    fptr.write(str(total) + '\n')

    fptr.close()
