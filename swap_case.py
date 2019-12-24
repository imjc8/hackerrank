# 24/12/2019
# swap case challenge
# user inputs in a string, which the program then flips the case
# https://www.hackerrank.com/challenges/swap-case/problem

#function which flips the case
def swap_case(s):
    #takes in a string from main
    #initialise new_string as a string
    new_string = ''

    #find length of the string passed into the function
    length = len(s)
    #print(length)

    #loop through the string
    for i in range(0, length):
        #if the char is upper case, convert to lower
        if s[i].isupper():
            #concatenate the flipped char onto the new string
            new_string = new_string + s[i].lower()
        else: # char is lower, flip to upper
            new_string = new_string + s[i].upper()
    
    #return the new string to the main function
    return new_string

if __name__ == '__main__':

    #user inputs a string to variable s
    s = input()
    #call the function
    result = swap_case(s)
    #print result
    print(result)




