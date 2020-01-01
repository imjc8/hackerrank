#!/bin/python3
# 01/01/2020
# https://www.hackerrank.com/challenges/the-birthday-bar/problem

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    #the month 'm' represents how many blocks she wants to give
    #the day has to be the sum of the values on blocks continuously
    #return how many ways, these conditions can be met

    #initialise counter - store how many ways the condition can be met
    counter = 0

    #initialise array
    arr = []

    #length of list
    length = len(s)

    #length-m+1 is the equation to look at continuous blocks
    #draw out array and cycle through to get equation
    for i in range(length - m + 1):
        arr = s[i:m+i]
        #get sum of array
        result = sum_array(arr)

        if (result == d):
            counter = counter + 1
        
        else:
            continue
    return counter

#function to return sum of an array
def sum_array(a):
    #length of list
    length = len(a)
    #total variable to count up the sum
    total = 0
    #iterate through list
    for i in range(length):
        total = total + a[i]
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #user input number of chocolate blocks
    n = int(input().strip())
    #user input chocolate blocks
    s = list(map(int, input().rstrip().split()))
    #get user input
    dm = input().rstrip().split()
    #assign date and month from above user input
    d = int(dm[0])
    m = int(dm[1])
    #function call
    result = birthday(s, d, m)
    #print and write result
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()

