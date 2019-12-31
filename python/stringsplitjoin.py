# 31/12/2019
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# this program splits a string and joins them with '-'

def split_and_join(line):
    # split string by a space into a list of words
    a = line.split(" ")
    # join list entries with a '-'
    a = "-".join(a)
    # return value
    return a
if __name__ == '__main__':
    #user input line
    line = input()
    #call function
    result = split_and_join(line)
    #print
    print(result)