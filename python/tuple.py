# 24/12/2019
# tuple practice in hackerrank
# https://www.hackerrank.com/challenges/python-tuples/problem
# takes in a number, which represents the number of numbers in the tuple
# mapped into integer list
# converted to tuple
# hashed

if __name__ == '__main__':
    #get user input for how many numbers in the tuple
    n = int(input())

    #space separated numbers entered by user to be in tuple 't'
    integer_list = map(int, input().split())
    
    #tuple 't'
    t = tuple(integer_list)
    for i in range(0, n):
        result = hash(t)

    print(result)
