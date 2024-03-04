# functions 1/3


# + Topic 1: Function What and Why
#   - what: is a group of statements for a specific task 
#   -examples: print(), input(), int(), float(), round()

# why: reusability, & modulatrity (divide and conquer) split into substasks 
#       easy to read, write & debug / cooperation
# two types: 
#           1. Void function: just do something, no data carried back
#               -print()
#           2. value-returning function: return data back to the user/caller
#                  -input(),int(), float(), uses return statement

# + Topic 2: Function How
#               -Defining a function: def function_name(parameters):
#                                           statements
#
#   -Naming: same rules as naming a variable
#           - no keyword, first_ or letter, others _, letters, digits + no space or special symbols 
#           - follows a style (snake_case), has meaningful/descriptive name

# Example 1: a fucntion that prints messages
def print_messages():
    print('Hello, Welcome to Python')
    print('Hope you enjoy it, but you have to do it')

# Example 2: a function that reads an int 19-59 until a valid one, then prints 'good' (lab 0)
def read_int():
    x = int(input('x = '))
    while x <19 or x > 59: 
        x = int(input('x = '))
    print('good')

# Example 3: a function reading two integers, print multiples of 7 in between
def multiple_seven():
    x, y = int(input('Number 1: ')), int(input('Number 2: '))
    if x > y: x, y = y, x
    print('Multiple of 7: ', end ='')
    for n in range (x, y+1):
        if n % 7 == 0: print(n, end =' ')

# we need to call function to execute it 
        #Calling function: 
        # how: function_name()  [not usually called this way in practice]
        # a function can be called many times, from mnay places
            # Note: recursive function - a function is able to call itself
        # a function can call a function within a function
        # by practice the first function called is named main():
'''def main():
    print_messages()
    read_int()
    multiple_seven()'''


#           What happens: 
#                       1. jumps to the function being called
#                       2. executes the called function 
#                       3. jump back to caller function
#                  - pass statements: does nothing, useful when used in a skeleton function
#    Example: 
def fun9():
    pass 


#
# + Topic 3: - Passing data to function
#            - Example: print(value1, values2, value3,...)
#            - int(string), round(value,number)
#   
#     -def function name(parameters)
#     -can be zero or contain multiple paramenets
#     -multiple parameters are seperates by commas
#     - Parameters: a.k.a formal parameters
#           - in function definition
#     - Arguments: a. k. a actual parameters 
#           - values used in calling a function
#           - optional argument: has deault value
#              name=value
#           - passing by position: positional arguments
#           - passing by name: order doesn't matter

# Example: a fucntion that takes/accepts/is given two integers, lower and upper
#           the function reads an integer within the range of lower to upper

def get_int(lower, upper):
    x = int(input(f'Enter and int between {lower} and {upper}'))
    while x < lower or x > upper: 
        x = int(input(f'Enter and int between {lower} and {upper}'))
    print(f'Got a good number: {x}')

def topic3_test():
    get_int(1, 20)
    get_int(50,80)

# + Topic 4: More parameters
    # Parameters are local variables 
    # Local Variables are defined in functions
    # has a function scope(where can access it)
    # multiple functions have variable of the same name

def fun1(x,y):
    a = 123

def fun2():
    a = 234