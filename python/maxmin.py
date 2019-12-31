#!/bin/python3
# 01/01/2020
# https://www.hackerrank.com/challenges/mini-max-sum/problem
# given an array with 'n' number of elements
# find the maximum and minimum sum of 'n-1' elements

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    #sort string with min to max
    minfirst_list = sorted(arr)
    #sort string with max to min
    maxfirst_list = sorted(arr, reverse = True)

    #initialise variables to hold the min and max sums
    max_sum = 0
    min_sum = 0
    #length of list
    length = len(arr)
    #iterate through list, first 'n-1' elements of each list
    for i in range(0,length-1):
        #this list will give us the min sum since maximum value is ignored in list
        min_sum = min_sum + minfirst_list[i]
        #gives us max sum as it uses the highest 'n-1' numbers
        max_sum = max_sum + maxfirst_list[i]

    #print values with space separation
    print(min_sum, end = ' ')
    print(max_sum)


if __name__ == '__main__':
    #user inputs array
    arr = list(map(int, input().rstrip().split()))
    #call function
    miniMaxSum(arr)
