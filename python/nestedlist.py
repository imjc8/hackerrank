# 24/12/2019
# this program takes in a list from user input
# the inputs include name and mark from that student
# it then returns the students with the 2nd lowest mark
# names are printed in alphabetical order

#function to sort the results from the students into ascending order
def sortlist(some_list):
    return(sorted(some_list, key = lambda x: x[1]))

#main
if __name__ == '__main__':
    #list of students and their results, this list is not ordered
    student_list = []
    #list containing the names of students with the second lowest mark
    name_list = []

    #prompt user to enter the number of students
    #print('Enter number of students')
    number = int(input())
    for i in range(number):
            name = input()
            score = float(input())
            student_list.append([name, score])
    #this list has the marks ordered
    ordered_list = sortlist(student_list)
    
    #return the 2nd lowest mark
    i = 0
    low1 = ordered_list[i][1]
    for i in range(0, number):
        if ordered_list[i][1] > low1:
            low2 = ordered_list[i][1]
            break
        else:
            i = i + 1
    
    #make list with names with results of certain value
    i = 0
    for i in range(0, number):
        if ordered_list[i][1] == low2:
            name = ordered_list[i][0]
            #print(ordered_list[i][0])
            name_list.append(name)
        else:
            i = i + 1

    #sort names into alphabetical order
    name_list.sort()
    for i in range(0, len(name_list)):
        print(name_list[i])
    