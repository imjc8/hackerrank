#!/bin/python3
# 01/01/2020
# first program of new year, at 12:30am
# https://www.hackerrank.com/challenges/plus-minus/problem

#find ratio of positive, negative and zero items in an array

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    #initialise counters
    positive = 0
    negative = 0
    zero = 0
    #total elements in the array
    total = len(arr)
    for i in range(0, total):
        #if positive, increment positive counter
        if arr[i] > 0:
            positive = positive + 1
        #if equal to zero, increment zero counter
        elif arr[i] == 0:
            zero = zero + 1
        #else it has to negative, so increment negative counter
        else:
            negative = negative + 1
    positive_ratio = positive/total
    negative_ratio = negative/total
    zero_ratio = zero/total

    print('{0:.6f}'.format(positive_ratio))
    print('{0:.6f}'.format(negative_ratio))
    print('{0:.6f}'.format(zero_ratio))
    


if __name__ == '__main__':
    #user input how many elements in array
    n = int(input())
    #creates a list which maps out the user inputted elements
    arr = list(map(int, input().rstrip().split()))
    #call function
    plusMinus(arr)
