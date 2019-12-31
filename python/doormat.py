# 31/12/2019
# https://www.hackerrank.com/challenges/designer-door-mat/problem
# print out welcome mat given certain dimensions from user
# user inputs 'm and n' where m is odd, n = m* 3
# print out a certain pattern
'''    
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''

if __name__ == '__main__':
    #prompt user to import dimensions
    m, n = input().split()

    #strings bunched up
    dash = '---'
    fill = '.|.'

    #conver to ints
    n = int(n)
    m = int(m)

    #since strings can be bundled into 3 chars, overall length is divided by 3
    a = int(n/3)

    #occurence for middle row
    occur3 = int((n-7)/2)

    #for first half of mat
    counter1 = int(m/2)

for i in range(0, int(m)):
    #print(i)
    if i == int(m/2):
        print(occur3 * '-', end = '')
        print('WELCOME', end = '')
        print(occur3 * '-')
    elif i < counter1:
        occur1 = counter1 - i
        occur2 = 2*i + 1
        print(occur1*dash, end = '')
        print(occur2*fill, end = '')
        print(occur1*dash)
    
    #print reverse of what is above
    else:
        print(occur1*dash, end = '')
        print(occur2*fill, end = '')
        print(occur1*dash)
        occur2 = occur2 - 2
        occur1 = occur1 + 1