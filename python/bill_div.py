#!/bin/python3
# 01/06/2021
# https://www.hackerrank.com/challenges/bon-appetit/problem

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill - list consisting the price of each item ordered
#  2. INTEGER k - item anna does not eat
#  3. INTEGER b - amount charged
#

def bonAppetit(bill, k, b):
    # Number of items
    num_items = len(bill)
    # item anna did not eat
    skip_ind = k

    # remove item from the bill using index position
    del bill[k]
    
    # total from bill 
    bill_total = sum(bill)

    anna_pay = bill_total/2
    #print('anna',anna_pay)
    #print('charged',b)

    if anna_pay == b:
        print('Bon Appetit')

    else:
        print(int(b-anna_pay))
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
