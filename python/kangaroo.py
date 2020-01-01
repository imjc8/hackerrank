#!/bin/python3
# 01/01/2020
# https://www.hackerrank.com/challenges/kangaroo/problem

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    #since we are given x1<x2, if v2>=v1, k1 will never catch up
    #the kangaroo must fulfil the following equation
    # x1+y*v1 = x2+y*v2
    #make y the subject : y = ((x1-x2)/(v2-v1))
    #if y is not a whole number, means that there needs to be partial jumps
    #therefore the modulo needs to be 0, for it to meet
    if (v2 >= v1 or ((x1-x2)%(v2-v1)) != 0 ):
        return 'NO'
    else:
        return 'YES'
    

if __name__ == '__main__':
    #write to output path
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #user input, space separated [k1 start position, speed, k2 start position, speed]
    x1V1X2V2 = input().split()
    #assign values
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    #function call
    result = kangaroo(x1, v1, x2, v2)
    #print and write to file
    print(result)
    fptr.write(result + '\n')

    fptr.close()
