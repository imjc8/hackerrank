#!/bin/python3
# 01/01/2020
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    #computes the pairs of elements, where when summed, is divisible by 'k'

    #initialise counter
    counter = 0

    #initialise sum
    sum_total = 0
    #iterate through array
    for i in range(n):
        #iterate though the pairs
        for j in range(n-i-1):
            sum_total = ar[i] + ar[j+1+i]
            #if no remainder
            if (sum_total%k == 0):
                counter = counter + 1
                #troubleshoot msg
                #print('numbers are: ' + str(ar[i]) + ' and  ' + 
                    #str(ar[j+1+i]) + ' ij:  ' + str(i) + ' ' + str(j+1+i))
            else:
                continue
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #user input, space-separated
    nk = input().split()
    #number of elements
    n = int(nk[0])
    #divisible number
    k = int(nk[1])
    #store an array that is space-separated, entered by user
    ar = list(map(int, input().rstrip().split()))

    #call function
    result = divisibleSumPairs(n, k, ar)
    #print and store result
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()