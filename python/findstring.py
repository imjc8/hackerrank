# 28/12/2019
# https://www.hackerrank.com/challenges/find-a-string/problem
# find the occurence of a substring within a main string
# eg - main string is 'abcdcdc' - substring is cdc
# output should be 3

#function to count the occurence of substring
#done by comparing a 'block' of chars from the substring to the main string
def count_substring(string, sub_string):
    #initialise counter
    counter = 0

    #loop through the main string until the last char, which coresponds to 
    #length of main string - length of substring + 1
    for i in range(0, len(string) - len(sub_string) + 1):
        #if the blocks or chars are equal, increment counter
        if string[i:(i + len(sub_string))] == sub_string:
            counter = counter + 1
        #increment i
        else:
            i = i + 1
    return counter

if __name__ == '__main__':
    #prompt user for string
    string = input().strip()
    #prompt user for substring
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


''' 
old function, does not work

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
'''