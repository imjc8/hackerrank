# 28/12/2019
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    counter = 0
    for i in range (0, len(string)):
        for j in range(0, len(sub_string)):
            if (sub_string[j] == string[i+j] and i+j == len(string)):
                counter = counter + 1
            else:
                break
    counter = counter/len(sub_string)
    return int(counter)

if __name__ == '__main__':
    #prompt user for string
    string = input().strip()
    #prompt user for substring
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)