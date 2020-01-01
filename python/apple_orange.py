#!/bin/python3
# 01/01/2020
# https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #s - start point of house
    #t - end point of house
    #a - location of apple tree
    #b - location of orange tree
    #apples - integer array showing the distance from each tree
    #oranges - integer array showing the distance from each tree
    
    #initialise counters
    counter_A = 0       # the number of appples that land in house
    counter_B = 0       # the number of oranges that land in house

    #for apples
    for i in range(len(apples)):
        #translate from local apple tree reference to global reference
        apples[i] = apples[i] + a       #integer array for location

        #check bounds, if 's =< apples[i] <= t'
        if (s <= apples[i] <= t):
            counter_A = counter_A + 1
        else:
            continue
    
    #for oranges
    for i in range(len(oranges)):
        #translate from local orange tree reference to global reference
        oranges[i] = oranges[i] + b       #integer array for location

        #check bounds, if 's =< oranges[i] <= t'
        if (s <= oranges[i] <= t):
            counter_B = counter_B + 1
        else:
            continue

     #print values
     print(counter_A)
     print(counter_B)   
     
    return 0

if __name__ == '__main__':
    
    #user input, space separated, for s and t (position of house)
    st = input().split()
    #assignment from the input above
    s = int(st[0])
    t = int(st[1])

    #user input, space separated, for a and b (location of each tree)
    ab = input().split()
    #assignment from the input above
    a = int(ab[0])
    b = int(ab[1])

    #user input, space separated, for m and n (number of apple/orange)
    mn = input().split()
    #assignment from the input above
    m = int(mn[0])
    n = int(mn[1])

    #create list
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    #print(apples)

    #call function
    countApplesAndOranges(s, t, a, b, apples, oranges)
