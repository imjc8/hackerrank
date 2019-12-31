#!/bin/python3
# 01/01/2020
# https://www.hackerrank.com/challenges/time-conversion/problem
# EXPECTED
# input 07:05:45PM
# output 19:05:45
import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #if hour starts with 12, we need to check if its 'AM' or 'PM'
    if s[:2] == '12':
        #if 'PM' ending, we dont change anything except get rid of ending
        if s[8:] == 'PM':
            s = s[0:8]
        #it is 12AM, we need to change hh to '00'
        else:
            hh = '00'
            s = hh + s[2:8]
    
    #if the ending is AM, we just leave it and get rid of ending
    elif s[8:] == 'AM':
        s = s[0:8]
    #if ending is PM, we add 12 and get rid of ending
    else:
        hh = int(s[0:2]) + 12
        s = str(hh) + s[2:8]
    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    #user inputs a the time, stored as a string
    s = input()

    #call function
    result = timeConversion(s)
    #print result
    print(result)
    #write result to file
    f.write(result + '\n')
    #close file
    f.close()
