#!/bin/python3
# 03/01/2021
#https://www.hackerrank.com/challenges/python-string-formatting/problem

#1<n<100
#print in columns : dec / octal / Hex / binary
def print_formatted(number):
    #your code here
    #initialise string
    prnt_str = ''
    #finding the width of the number - max width will be binary rep of number
    bin_input = bin(number)[2:]
    num_width = len(bin_input) + 1
    for i in range (number):
        #decimal
        dec_num = i + 1
        dec_num =str(dec_num)
        #octal - will break for negative integers, but we dont have any
        oct_num = oct(i+1)[2:] 
        #hex
        hex_num = (hex(i+1)[2:])
        hex_num = hex_num.upper()
        #binary
        bin_num = bin(i+1)[2:]

        #print
        prnt_str = dec_num.rjust(num_width - 1, ' ') + oct_num.rjust(num_width, ' ') + hex_num.rjust(num_width, ' ') + bin_num.rjust(num_width, ' ')
        print(prnt_str)

if __name__== '__main__':
    n = int(input())
    print_formatted(n)


