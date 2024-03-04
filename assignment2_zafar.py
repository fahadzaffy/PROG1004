# Name: Fahad Zafar
# Class: PROG1004, P03, Winter 2024
# Assignment: Assignment #2
# Date: Feb 19, 2024

# Description: A program that simulates a six sided dice roll

import assignment2_zafar_helpers
#imported helper functions from helper file to use in main app

#will define the main function and assign a value 
#to rolling times which will be the the number 
#user enters in the valid_number function 
# so only the allowed cases are run

def main():
    while True: #using condition while to run main function over and over

    #since we didn't define rolling times in the helper file 
    # I will define it to take the number the user inputs from valid_number 
    # we need to set the arguments for valid number 

        rolling_times = assignment2_zafar_helpers.valid_number(lower=0, upper=10000, 
        error='Invalid number',prompt='Rolling Times(1-10000, 0 to stop) : ')

    #writing the condition if the user inputs 0 
    #the program will stop and print 'Thank you' message 
    #otherwise we will run function 2 diceroll with 
        if rolling_times == 0:
            print("Thank you")
        else:
            one, two, three, four, five, six = assignment2_zafar_helpers.dice_roll(
            rolling_times)
            #setting the variables of each dice face to be equavilent to the count tallies
            #returned by the dice_roll function 
            max_count = max(one, two, three, four, five, six) 
            #taking the max count for each face above
            scale = 70 / max_count #scaling to 70 characters 

            #calling the function printline from helper file and passing the arguments
            #printline function is called six times for each of the faces of the dice
            
            
            assignment2_zafar_helpers.printline("One",round(one * scale), '=', one)
            assignment2_zafar_helpers.printline("Two",round(two * scale), '=', two)
            assignment2_zafar_helpers.printline("Three",round(three * scale), '=', three)
            assignment2_zafar_helpers.printline("Four",round(four * scale), '=', four)
            assignment2_zafar_helpers.printline("Five",round(five * scale), '=', five)
            assignment2_zafar_helpers.printline("Six",round(six * scale), '=', six)
            #using the round function to round to an integer 


if __name__ == "__main__":
    main()



    