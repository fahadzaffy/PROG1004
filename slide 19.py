#You would like to be able to calculate your average
#grade for all the courses you've taken in first
#semester. Write a program that prompts you for the
#grades for the five courses you would have
#completed in first term. After recording all five
#grades, display the average grade on the console.
#• Sample output using sample data:
#–You entered your five grades as: 85.6 78.9
#75.5 90.0 86.5 Your average grade: 83.3 


grade_1 = float(input('Enter the first grade: '))
grade_2 = float(input('Enter the second grade: '))
grade_3 = float(input('Enter the third grade: '))
grade_4 = float(input('Enter the fourth grade: '))
grade_5 = float(input('Enter the fifth grade: '))
average = grade_1 + grade_2 + grade_3 + grade_4 + grade_5 / 5

print(f'You entered:', {grade_1}, {grade_2}, {grade_3}, {grade_4}, {grade_5}, 
      f'Your average is: {average}')