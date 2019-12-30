# 28/12/2019
# https://www.hackerrank.com/challenges/whats-your-name/problem
# this program receives 2 inputs from user, representing their first and 
# last names on 2 separate lines, then inserts them to form a sentence

def print_full_name(a, b):
    print("Hello " + a + ' ' + b + '! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)