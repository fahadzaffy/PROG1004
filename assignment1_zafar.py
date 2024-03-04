# Name: Fahad Zafar
# Class: PROG1004, P03, Winter 2024
# Assignment: Assignment #1
# Date: Jan 30th, 2024

# Description: An application that gets user input of two positive integers 
# and compares them to each other outputting a message of whether the integers
# are greater/smaller or equal to another

#setting inital flag to be true
play_again = True
#setting while loop to execute when flag is true repeatedly
while play_again == True:
    # declaring x to be first integer user inputs 
    x = int(input('Enter the first positive integer: ')) 
    while x <= 0:  #using while loop to restrict user integer to positive integers
        # Error message is printed when input is negative
        print('Error: Number must be positive!')
        # repromt user to avoid infinte loop
        x = int(input('Enter the first positive integer: ')) 
    
    # defining y to be second integer user inputs 
    y = int(input('Enter the second positive integer: '))  
    while y <= 0:  #using while loop to restrict user input to positive integers
         # Error message is printed when input is negative
        print('Error: Number must be positive!')
        # repromt user to avoid infinte loop
        y = int(input('Enter the second positive integer: ')) 

    #printing statements for all 3 scenarios:
    if x > y :  
        print(x, 'is greater than', y)
    if x < y :
        print (x, 'is less than', y)
    elif x == y : 
        print('The two numbers are equal') 

    
    print(f'The common factors of {x} and {y} are: ', end = ' ')    
    #declaring variable i as common factors
    for i in range (1, x+1) and range (1, y+1) : 
        # checking for both x and y values from 1 until it reaches x and y 
        # (variable+1) to make sure actual x and y values are not excluded
        if x % i == 0 and y % i == 0: #common factors will return remainder of zero
          print(i, end = ' ') # printing factors and formatting end to display on one line

    print('\n') #new line spacing for next prompt

    #promting user to input whether they want to run program again
    answer = (input('Play again? (Y/y) or (N/n): ')) 
    #restricing user input to set of answers with while loop
    #if answer is not in set user is prompted again until valid response is given
    while answer != 'Y' and answer != 'y' and answer != 'N' and answer != 'n':
        print('Error: choice must be (Y/y) or (N/n) ')
        answer = (input('Play again? (Y/y) or (N/n): '))
    #covering all scenarios:
    #setting flag to change to true for yes values (Y/y)
    #setting flag to change to false for no values (N/n)
    if answer == 'Y' : play_again = True
    elif answer == 'y' : play_again = True
    elif answer == 'N' : play_again = False
    elif answer == 'n' : play_again = False



    
    
