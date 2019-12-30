# 28/12/2019
# https://www.hackerrank.com/challenges/python-mutations/problem
# demonstrates the properties of strings
# mutability and immutability

def mutate_string(string, position, character):
    #convert string into a list
    l = list(s)
    l[position] = character
    s_new = ''.join(l)
    return s_new

if __name__ == '__main__':
    #input string
    s = input()
    #input position and char you want to insert
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)