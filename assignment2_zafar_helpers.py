# Name: Fahad Zafar
# Class: PROG1004, P03, Winter 2024
# Assignment: Assignment #2
# Date: Feb 19, 2024

# Description: helper module containing functions to 
#  simulate 6 sided dice rolls for a number of times 
# and print the results in a formatted line with the total number of counts 
# for each time a face of a dice appears in the number of rolls

    
# valid_number prompts the user to enter an intege
# if integer is lower than 0 or greater than 10000
# it will display an error 'Invalid number'
# then reprompt the user for a valid input

import random
def valid_number(lower, upper, error, prompt):
    num = int(input(prompt))
    while num < lower or num > upper:
        print(error)
        num = int(input(prompt))
    else:
        return num

# dice_roll function will take the returned int number 
# from the valid_number function as input 
# for the number of times the user rolls the dice
# then the function will accumilate the totals each face is rolled 
    
def dice_roll(rolling_times):
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    for _ in range(rolling_times): 
        dice_face = random.randint(1,6) #rand.randint is inclusive
        if dice_face == 1: counter1 += 1
        elif dice_face == 2: counter2 += 1
        elif dice_face == 3: counter3 += 1
        elif dice_face == 4: counter4 += 1
        elif dice_face == 5: counter5 += 1
        elif dice_face == 6: counter6 += 1
        # counts are accumulated/totaled and returned by function 
        #for the # of rolls
    return counter1, counter2, counter3, counter4, counter5, counter6
   

# The third function printline will print out the results of the diceroll
# on the screen in formatted output where the ==== line's length
# depends on the number of times each face appears 
# (more times a face appears the longer the line of '=' is )
# with the total number of times that face was rolled
# need to scale the length of '=' to less than 70 characters
# finally at the end of the ==== 
# we want to print out the total times that face was rolled
# For example: 
# One :  =========== count
# Two : ================ count
# Three : ================== count
# Four : ================================ count
# Five : ============== count
# Six : ======================== count

def printline(title, length, char, note):
    print(f'{title}: {char * length} {note}')
    # this function does not return a value will take on arguments
    # that will be passed on to the parameters in the main file


