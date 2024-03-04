# %2 = 0 means an interger is even and if %2 !- 0 then the integer is odd

# Repetition - 1/3
# aka itertion or loops
# do something continously

# Two types of repetitions: 
#   1.) Condition-controlled loop (while loops / while statement)
#       - before we run loop, no idea how many times to run
#       - stops when condition is met

#   2.) count controlled loop (for statement/while statement)
#       - before we have loop, we already know how many times we need to run 


# Topic 1: While Statemennt 
#   -used for condition controlled loop
#   -Syntax: 
#           while condition:
#               statements
#   -Logic: 
#           check condition, if true then the statements in the block are executed
#           check condition, if true and execute statement
#           ... (keeps doing it over) until condition is false (finishes executing)
#             Note: pretest loop, if first time the condition is false then we do nothing

#Example: repeatly ask for sales and comission rate, print comission, until user does not have any more sales
'''
choice = 'y'
while choice == 'y':
    sale = float(input('Sales Amount: '))
    rate = float(input('Comission Rate: '))
    print(f'Comission is {sale * rate / 100:.2f}')
    choice = input('More sales (y-Yes, other-No): ')

a, b = 13424, 309798
answer = int(input(f'(a) + {b} = '))
while answer != a + b: 
        print('Incorrent, try again! ')
        answer = int(input(f'{a} + {b} = '))
print('Correect Answer')


#Example: repeatly asking the width and height of room and then print area until 
#         there are no more room

more_room = True
while more_room: 
      width, height = int(input('Width: ')), int(input('Height: '))
      print(f'The area is {width * height}')
      answer = input('Do you have more room (y-Yes, others-No)')
      if answer != 'y': more_room = False
'''
# Using while as a count-controlled loop

# Step 1: initialize counter
# Step 2: Comparasion in condition
# Step 3: Update the counter

'''
counter = 1  #step 1
while counter <= 10:  #step 2
      print(f'{counter}: I am sorry') 
      counter = counter +1  # Step 3 - update\
print('The counter is:', counter)
'''

# Topic 2: For statement
#   for count controlled loop
# syntax: 
#          for variable in a_sequence of values: can be a list, string or range()

# Logic: Assign value to varibale one by one, each time run block

for color in ['red', 'yellow', 'blue', 'green', 'black']: 
      print('Current color is: ', color)

# value is a string
      
for ch in 'Hello world':
      (print('Current chracter is:', ch))  # if value is a string: variable will be assigned character one by one


# function range(): generates a sequence of value automatically 
#   - range (start, stop, step) aree possible arguments *stop is exclusive*
#   - 1 argument: stop, by default start is 0, and step is 1
#   - range(5): 0, 1, 2, 3, 4

# 2 arguments: Start, Stop, Step is 1
#       range (10,16): 10, 11, 12, 13, 14, 15
      
# 3 Arguments: 
#       range (5, 35, 7): 5, 12, 19, 26, 33   
#       range (11, 21, 2): 11, 13, 15, 17, 19

    