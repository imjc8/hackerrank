#!/bin/python3
# 24/12/2019
# python program which capitalises the first letter of each word
# finish the function
# https://www.hackerrank.com/challenges/capitalize/problem

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    #initialise the function
    new_string = ''

    #get length of the string
    length = len(s)

    #initialise a flag, this will be 1 if a space is detected
    flag = 1

    #loop through the string
    for i in range(0, length):
        #if a space is detected, it means next letter that comes up must be capital
        if s[i] == ' ':
            #set flag
            flag = 1
            #add character to the new string
            new_string = new_string+s[i]

        #if the flag is up and a lowercase letter is detected
        elif flag == 1 and s[i].islower():
            #convert to upper case
            new_string = new_string + s[i].upper()
            #reset flag
            flag = 0
        
        #handles all other cases such as upper case already, lowercase words, etc
        else:
            #add to string
            new_string = new_string+s[i]
            #set flag to 0
            flag = 0
    #return the new string to the main function    
    return new_string
    

if __name__ == '__main__':
    
    #cannot run on pc if this is here, but is give by the challenge
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
    '''
# to fix this and run on my pc, i use this
    s = input()
    result = solve(s)
    print(result)