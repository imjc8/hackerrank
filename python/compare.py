#!/bin/python3
# 31/12/2019
# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen
# compare marks between 2 people, if 1 is greater than the other, give 1 mark
# if they are the same, give no marks

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    scores = [0, 0]
    for i in range(0, len(a)):
        if a[i] > b[i]:
            scores[0] = scores[0] + 1
        elif a[i] < b[i]:
            scores[1] = scores[1] + 1
        else:
            continue
    return scores
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    
    fptr.write('\n')

    fptr.close()