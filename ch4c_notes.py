'''
 Write a program that prints a menu as below
1. Addition
2. Subtraction
3. Exit
Enter Your Choice: __
• When the user chooses 1 or 2, prompt the user to enter
two numbers, then prints the result
• When the user enters anything else, displays an error
message and prints the menu again
• When the user chooses 3, terminate the execution
'''


print(f'1. Addition' '\n'
      f'2. Subtraction' '\n'
      f'3. Exit' '\n')

user_choice = int(input('Please choose an option: '))
while user_choice != 1 and user_choice != 2 and user_choice != 3:
    print('Error: not a valid option')
    print(f'1. Addition' '\n'
      f'2. Subtraction' '\n'
      f'3. Exit' '\n')
    user_choice = int(input('Please choose an option: '))
    if user_choice == 1: 
        num_1, num_2 = int(input('Enter the first number:')), int(input('Enter the second number'))
    
