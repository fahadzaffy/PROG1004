#Coding question 1:
# write a program that allows a student to complete a registration
# form or displays a completion message that includes a welcome message
# or a login name. The login consists of the user's last name
# the users student ID

#Example:
# Last Name : 
# Student ID : 
# Welcome, your login name is : LastnameStudentID#

last_name = input('Last name : ')
student_id = input('Student ID : ')
print(f'Welcome, your login name is : {last_name}{student_id}')

#Coding question 2: 
# write a program that calculates the tip or total for a meal at the restaurant
# the formula for calculating the tip is tip = cost of meal * (tip percent / 100)
# Assume the user will enter valid data 
# the program should round the results to two decimal places 

# sample: 
# Cost of meal: 35.41
# Tip Percent: 
# Tip amount: 6.73
# Total amount: 42.14


mealcost = float(input('Cost of meal: '))
tip = float(input('Tip %: '))
print(f'\nCost of meal: {mealcost}'
      f'\nTip percent: {tip}'
      f'\nTip amount: {mealcost * (tip / 100) : .2f}'
      f'\nTotal amount: {mealcost * (tip/100) + mealcost: .2f}')


# Question 3
# Write a program to process the students marks 
# First, read the number of students 
# Then read all marks one by one 
# Finally print the number of marks in grade 
# A[90-100], B[80-90], C[65-80], D[50-65], F[0-50]
# round average to two decimal place 
# user input is read


students = int(input('\nNumber of students: '))
totalmarks, a, b, c, d, f = 0, 0, 0, 0, 0, 0 
# you can have multiple accumulator variables make sure to seperate with commas if in one line
for _ in range (students): #double for loop one for the number of students 
    for i in range(5): # we know we have to make 5 inputs so we will iterate 5 inputs for marks.
                       # +1 in the prompt string because in the first iteration it will be 0+1 = 1, second iteration 1+1 = 2, 
                       # 3rd iteration 2+1 = 3, 4th 3+1 = 4 and fifth iteration 4+1 = 5
        mark = float(input(f'Mark{i+1}:'))  
        totalmarks += mark
        if mark >= 90:
            a += 1
        elif mark >= 80:
            b += 1
        elif mark >= 65:
            c += 1
        elif mark >= 50:
            d +=1
        else:
            f += 1
    average = totalmarks/(students * (i+1)) # need to multiply the number of students by the number of iterations in i
print(f'A:{a}, B{b}, C:{c}: D:{d}, F:{f}'
      f'\nAverage: {average:.2f}')