# 24/12/2019
# Dictionary
# student names and their results for math, physics and chemistry is put into
# a dictionary
# student_marks1 = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
# user will query a name, and the average of the test results will be printed to 2d.p


from decimal import Decimal

if __name__ == '__main__':
    student_marks1 = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
    n = int(input())
    student_marks = {}
    value_list = []

    #for personal use, take out the next comment block
    ##################################
    '''
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    '''
    ##################################

    #get user input for the name to look up
    query_name = input()

    #check if name is in the dictionary
    #if you can find it in the dictionary
    if query_name in student_marks1:
        #assign the value for the key(student name) to value_list
        #for personal use, rename the students_marks1 to student_marks
        value_list = student_marks1.get(query_name, 0)
        print(value_list)

        #initialise result, used to add up the numbers
        result = 0

        #loop to add up the values in the list
        for i in range(0,3):
            result = result + value_list[i]
        
        #used to find the average
        #use decimal module to round up and display to 2dp
        average = Decimal(result/3)
        output = round(average, 2)
        print(output)
    
    #if name is not in dictionary
    else:
        print('Name not in dictionary')