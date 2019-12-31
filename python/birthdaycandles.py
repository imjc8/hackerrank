#!/bin/python3
# 01/01/2020
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    #sorts list from max to min
    sorted_list = sorted(ar, reverse = True)
    #length of list
    length = len(sorted_list)
    #maximum in the list will always be the first element
    max = sorted_list[0]
    #initialise counter to find the max
    counter = 0
    #check occurences of the max

    #iterate through list
    #this is the optimised method of finding max occurences since they are at
    #the front of the list
    #if its not equal to the max, it will break out
    for i in range(0, length):
        if sorted_list[i] == max:
            counter = counter + 1
        else:
            break
    #print(counter)
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #user inputs number of elements
    ar_count = int(input())
    #user inputs array elements, space-separated
    ar = list(map(int, input().rstrip().split()))
    #call function
    result = birthdayCakeCandles(ar)
    #write result to file
    fptr.write(str(result) + '\n')
    #close
    fptr.close()