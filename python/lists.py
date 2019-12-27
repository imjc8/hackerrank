# 27/12/2019
# https://www.hackerrank.com/challenges/python-lists/problem

#regular expressions package
import re

# main
if __name__ == '__main__':
    #number of commands by the user
    N = int(input())

    #initialise list
    mylist = []

    #loop through the number specified by user
    for i in range(0, N):

        #user input is put into a string called command
        command = str(input())
        
        #check if 'insert' is in the string
        #if it is, insert 'position' 'value'
        if "insert" in command:
            #finds all the integers in the string, returns list of
            #space-separated integers
            comm_list = (re.findall('\d+', command))
            #assign the corresponding values in the list to variables
            position = int(comm_list[0])
            value = int(comm_list[1])
            #use insert method
            mylist.insert(position, value)

        #if 'print' is in the command, print the list
        elif "print" in command:
            print(mylist)
        
        #if 'remove' is in the command, remove the first occurence
        #of specified value
        elif "remove" in command:
            #retrieve ints from the command string
            comm_list = (re.findall('\d+', command))
            #assign value from the list consisting ints
            value = int(comm_list[0])
            #remove
            mylist.remove(value)
        
        #if 'append' is in the command, append the value to the end of list
        elif "append" in command:
            #retrieve ints from the command
            comm_list = (re.findall('\d+', command))
            #assign value in list
            value = int(comm_list[0])
            #append method
            mylist.append(value)
        
        #if 'sort' is in the command
        elif "sort" in command:
            # sort the string using the sort method
            mylist.sort()
        
        #if 'pop' is in the command
        #if so, pop the last element from the string
        elif "pop" in command:
            #retrieve the length of the list
            length = len(mylist)
            #pop the last element, which is the 'length - 1'
            mylist.pop(length - 1)

        #if 'reverse' is in the command
        #if so, reverse the list
        elif "reverse" in command:
            #reverse string using reverse method
            mylist.reverse()

        #if command does not exist...
        else:
            print('Invalid Input')
        

        

