#!/bin/python3
#01/01/2020
#https://www.hackerrank.com/challenges/staircase/problem
# prints a staicase such as 
'''
4
   *
  **
 ***
****
'''

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    #initialisation
    space = ' '
    asterisk = '#'
    #iterate through loop
    for i in range(0, n):
        #print spaces
        print((n-1-i)*space, end = '')
        #print asterisks
        print((i+1)*asterisk)

if __name__ == '__main__':
    #user input for number of elements
    n = int(input())
    #call function
    staircase(n)
