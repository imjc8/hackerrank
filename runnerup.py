# 23/12/2019
# Hacker rank find runner up challenge
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# this program takes in a list of numbers and finds the 2nd highest

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

#sort list
inputlist = sorted(list(arr))

j = len(inputlist) - 1
#find the runner up
for i in range(len(inputlist)):
    if inputlist[j] != inputlist[j-i]:
        runnerup = inputlist[j-i]
        break
    else:
        i = i + 1

print(runnerup)
