
#!/bin/python3
# 01/01/21
# https://www.hackerrank.com/challenges/grading/problem

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    #find the length of 'grade' array
    length = len(grades)
    #print(grades)
    new_grades = []


    #iterate through array
    for i in range(length):
        #failing grade case
        remainder = grades[i]%5
        if grades[i] < 38 or remainder <= 2:
            continue
        else:
            grades[i] = grades[i] + 5 - remainder

    return grades



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #number of grades
    grades_count = int(input().strip())

    #array of grades this array is not rounded up
    grades = []

    #get user to input the grades and store into an array
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    #call function and store into result
    result = gradingStudents(grades)
    #print result
    print(result)
    #write result to file
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    