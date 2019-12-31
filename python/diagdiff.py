#!/bin/python3
# 31/12/2019
# https://www.hackerrank.com/challenges/diagonal-difference/problem
# finds the two sum of diagonals of a matrix
# then calculates the difference between the diagonals
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    #initiate sum variables
    left_diag = 0
    right_diag = 0
    #get the length of array, used to calc the right diag
    end = len(arr[0])
    #iterate through array
    for i in range (0, len(arr)):
        #left diag sum
        left_diag = left_diag + arr[i][i]
        #equation to calculate the right diag
        right_diag = right_diag + arr[i][end - 1 - i]
    #difference between the 2 diagonals
    difference = abs(left_diag - right_diag)
    #return value
    return difference
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #fptr = sys.stdout

    #user input - number of rows and columns
    n = int(input().strip())

    arr = []
    #user inputs an array
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
