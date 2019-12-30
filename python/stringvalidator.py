# 30/12/2019
# https://www.hackerrank.com/challenges/string-validators/problem
# check if string has alphanumeric, alphabetical, digit, lowercase and uppercase char

if __name__ == '__main__':
    #user inputs a string
    s = str(input())
    
    #set conditions
    cond1 = 0   #contains alphanumeric 
    cond2 = 0   #contains alphabetical
    cond3 = 0   #contains digit (0-9)
    cond4 = 0   #contains lower case
    cond5 = 0   #contains upper case

    #pass string through condition 1
    for i in range(0, len(s)):
        #if true, set cond1 to 1 and break out of loop
        if s[i].isalnum():
            cond1 = 1
            break
        else:
            #set cond1 to 0
            cond1 = 0
    #pass string through condition 2
    for i in range(0, len(s)):
        #if true, set cond2 to 1 and break out of loop
        if s[i].isalpha():
            cond2 = 1
            break
        else:
            #set cond2 to 0
            cond2 = 0
    #pass string through condition 3
    for i in range(0, len(s)):
        #if true, set cond3 to 1 and break out of loop
        if s[i].isdigit():
            cond3 = 1
            break
        else:
            #set cond3 to 0
            cond3 = 0

    #pass string through condition 4
    for i in range(0, len(s)):
        #if true, set cond4 to 1 and break out of loop
        if s[i].islower():
            cond4 = 1
            break
        else:
            #set cond4 to 0
            cond4 = 0
    #pass string through condition 5
    for i in range(0, len(s)):
        #if true, set cond5 to 1 and break out of loop
        if s[i].isupper():
            cond5 = 1
            break
        else:
            #set cond5 to 0
            cond5 = 0
    #now print the conditions out
    #if 1, then print 'True'
    #else, print 'False'    
    if cond1 == 1:
        print('True')
    else:
        print('False')
    if cond2 == 1:
        print('True')
    else:
        print('False')
    if cond3 == 1:
        print('True')
    else:
        print('False')
    if cond4 == 1:
        print('True')
    else:
        print('False')
    if cond5 == 1:
        print('True')
    else:
        print('False')