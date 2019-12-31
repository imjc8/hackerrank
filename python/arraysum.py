#!/bin/python3
# 31/12/2019
# https://www.hackerrank.com/challenges/simple-array-sum/problem
# returns the sum of the elements in an array of variable length
import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    length = len(ar)
    total = 0
    for i in range(0, length):
        total = total + ar[i]
    #print(total)
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #fptr = sys.stdout

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
