#!/bin/python3
# 01/01/2020 
# https://www.hackerrank.com/challenges/migratory-birds/problem

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    #sort array
    arr.sort()
    #length of array
    length = len(arr)
    #initialise counter
    counter = 0
    #initialise lists
    unique = []     #stores unique numbers
    freq = []       #stores the unique numbers and their frequency
                    #[unique element, frequency]

    #traverse the array
    for i in range(length):
        #if it is not in unique, then add it into unique, counter will equal 1
        if arr[i] not in unique:
            unique.append(arr[i])
            counter = 1
            freq.append([arr[i], counter])

        #if it is in unique, change the occurence in the list of the last element
        #this is possible because the list is sorted
        #this means that if the element is not unique, the element and occurence 
        #can be found in the end of the freq list
        else:
            counter = counter + 1
            freq[len(unique)-1][1] = counter
    #print(freq)
    #sort by the second field, which is the frequency, max to min
    #this somehow sorted the first element too, need to look into it
    #we need to return the lowest element number, if identical occurences exist
    #sort somehow did this for me, tested it
    freq.sort(key = lambda x: x[1], reverse = True)
    #return the element with the max occurence
    return freq[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #user input, space-separated, number of elements in array
    arr_count = int(input().strip())
    #user input, space separated, array elements
    arr = list(map(int, input().rstrip().split()))

    '''
    for testing
    arr_count = 7
    arr = [1,1,4,4,4,5,1] 
    #arr = [1,1]
    '''
    #function call
    result = migratoryBirds(arr)

    #print and store result
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
