#!/bin/python3
# 31/12/2019
# calculates the sum of numbers input

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    total = 0
    for i in range(0, len(ar)):
        total = total + ar[i]
    return total
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    #how many numbers you want to put in
    ar_count = int(input())

    #puts the numbers the user inputs into a lsit
    ar = list(map(int, input().rstrip().split()))

    #call function
    result = aVeryBigSum(ar)

    #print result
    fptr.write(str(result) + '\n')

    fptr.close()
