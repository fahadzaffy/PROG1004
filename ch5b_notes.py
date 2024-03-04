#Functions contd


#Topic 1 : Global Variables
#       -defined outside any functions
#       -has a global scope; starting from where it is defined until the end of file
#       -can be accessed in and out of functions
#       -to modify global variables in a function you have to re-declare it
#       - redeclared by gloabl variable_name
#       -Note : Try and avoid using global variables as it is bad practice unless they are constants 
#       naming constants: ALL_CAPS


# Topic 2: Random Numbers
#       - Standard Library: contains pre-existing functions
#           -built in functions are able to be directly called and used
#              example: print(), input(), int(), float()
#      - Other functions must be first imported then used
#       example: random, math
#
#       -Random package: used to generate random numbers
#           -import random 
#           - used functions: random.function_name()
#           - random.randomint(), takes to parameters (lower & upper): return a random int between lower and upper, both inclusive
#           - random.randrange(start, stop, step): return a random int (parameters are the same as the range function)
#           - random.random() - returns a random float number between [0.0, 1.0)
#           - random.uniform() takes two parameters (lower, upper) and returns a random float number between lower and upper 
#
#
''' 
import random
def random_tester():
    print('Random integers: ', end= '')
    for n in range (10):
        x = random.randint(20,50)
        print(x, end =',')
    print()

def main():
    random_tester()
main()
'''


#Exercise: write a functions that accepts a number, throws a coin for a number of times, count and print heads and tails
import random
def throw_coin(times):
    heads, tails = 0, 0
    for _ in range(times):
        # get a random int, if 0 - head and if 1 - tails
        coin = random.randint(0,1)
        if coin == 0 : heads += 1
        else: tails += 1
    print(f'Heads: {heads}, Tails: {tails}')

def main():
    throw_coin(3)
    throw_coin(33)
    throw_coin(333)

main()

# Topic 3: Value-returining functions
#       - functions that carry data back to the caller
#       - input(), int(), float(), all functions in random()
#    -Prompted by using return statement to return a value or multiple values
#       - Use comma to seperate multiple values
#       -in calling function, assign to multiple values
#       -return value can be of any type
#           -return None (nothing to return)
#       -the returned value can be used in calling function anywhere a variable is
#
# Example: reads and returns the first name and last name that you get from user
'''
def get_names():
    firstname = input('Enter First Name: ')
    lastname = input('Enter Last Name: ')
    return firstname, lastname

def student_app():
    first, last = get_names()
    print(f'Hello {first} {last}')



#Example: a function that takes a lower and upper of a valid mark, read a valid mark and return

def get_mark(lower, upper):
    if lower > upper: return None
    mark = float(input(f'enter mark ({lower} - {upper}) '))
    while mark < lower or mark > upper:
        mark = float(input(f'enter mark ({lower} - {upper}) '))
    return mark


# Example: a function that takes a number of tests, read the mark. Finally, return the average

def get_average(num):
    if num < 1: return None
    total = 0.0
    for n in range (1, num+1):
        mark = get_mark(0, 100)
        total += mark
    return total / num


def main():
    student_app()
    average = get_average
    print(f'Average is: {average}')

main()
'''