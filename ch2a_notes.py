#hello 
# comments start with pound symbol (not part of code) makes easier for others to read code usually are statements to explain code
# in natrual language (python is formal language)
# python interpreter will ignore them 

#Assignment 1 posted worth 5%
#make sure to use only techniques taught in class ∂

#How to learn:
# listen, takes notes and practice/follow demo code in class in vs code for immediate testing
# after class review topics, read slides, textbook and notes

# "Questions?" Slide Marks the end/break of class 


#Topic 1 : How to write a program
#Topic 2: Program components

# +Program Development has 3 steps

# - 1) Design
#       1.1) Get Requirments 
#       1.2) Analyze requirements to get a solution (algorithm)
#           -algorithm is the order of actions to perform a task or solution
#           -representation of algorithm are in two forms psuedocode (fake code or description of solution in a natrual language) 
#            or flowchart (boxes for actions and -> for order of actions)

 
# - 2) Implementation
#       Write code, save them into file named XXXX.py
#       written code is known as source code 
#       if code is not working as intended we check code and fix errors (syntax errors, runtime errors)
#      + Syntax Error: Language you are writing to communicate with computer (occurs when breaking rules of language)
#           + print('Hello World) is missing quotes will produce syntax error same for print('Hello World

print('Hello World')    

#       + Runtime error: Runs but crashes along the execution of the program
#           usually happens when you do not define a variable i.e. print(abc) but abc is not defined all code before this is correct

#       +Logic Error : Code runs but does not function as expected (result is incorrect) aka "BUGS"

# - 3) Tetsing
#       -Given the input and compares the it against the output against the expected result or output

# IPO: General Structure of Algorithm 
#   - Input: generally from users, other examples are keyboard, mouse, other input devices or network, files etc...
#   - Processing: calculation, compressing, search, sort, transform... usually dependant on task we want to do
#   - Output: Display results, save into a file, led, play sound etc...

# Example: Calculate and print surface area and volume of a cylinder given the height and radius
# -input: user inputs radius and height r=radius and h=height
# -processing: calculation of area and calculation of volume (how we calculate the value)
#           +Area = 2*pi*r*r+h*2*pi
#           +Vol = pi*r*r*h
# -output: area and volume

# PROBLEM 1 ON SLIDE 16 DEFINE THE IPO
# I: Get inputs from user p=Principal Amount, r=Rate, n= the number of years 
# P: Calculate the value of the investment after n amount of years final amount = P (1+R)^n
# O: Output the value of the future investment after n amount of years (Final Amount)

#TOPIC 2 - PROGRAM COMPONENTS 

#   + Statements
#       -a command, basic unit, action to be carried out 
#       -block: is a group of statements for a very specific small task
#       -fucntion: pre written code we use in the python language used directly 
#           -functions may take arguments

# example: 
# block: print the steps of putting an elephant into a fridge

print ('1-Open the fridge door')
print ('2-put elephant in')
print('3-close fridge door')

print('Python is cool') #print is a function and the message is an arguement (print fucntion still works without argument output is blank line)


# + Data Types 

#   -strings: a string of text/sequence of characters in quotes single, double or tripple are all acceptable in different cases 
#       -triple quotes used for multiline strings
#       -double quotes used usually when you have single quote in your string or vise versa

#   -Intergers: whole numbers e.g. 1,2,3,4,5...
#   -Float: Numbers with Decimals 3.9, 4.9, 5.2, 6.2...
#   - fucntion type() checks the type of value

# data type representations : int = interger, float=float, str=string

print(123)
print(3.14)
print('I am', 25, 'years old') # you can seperate values by commas to print multiple values

print(type("abc"), type(123), type(-4.567))

# + Variables
#   -what: usually is a reference/representation to a value
#           -a named value, a container of a value
#           -variable values can be changed or reassigned, old values are wiped from memory 
#           -In python you can change the type of values for a variable while reassigning unlike other coding languages 
#           -Python language used dynamic 
#   How: variables
#       - define and initalize 
#           variable_name = inital_name
# example below: 

name = 'Jack Anna' #defined a variable, assigned an inital value
age = 18 #defined variable named age having an inital interger value of 18
salary = 34567.89 #defined variable salary and assigned inital value of 34567.89 which is a float

print('My name is', name, 'and I am', age, 'years old') 
print('and I make', salary, 'dollars per year')

# Naming variables: cannot use keywords to name variables (if, else, while, for etc.)
#                  first character must be _ or letter (a-z or A-Z)
#                  other characters must be _ or letters or digits 
#                  no spaces or special symbols (!@@#$%^&*())
#                  best convention is to name variables with a descriptive name so you know what it is about
#                  follow style (CamelCase, lowerCamelCase, snake_case) only choose one and stick to it in your code!


#-Python allows you to assign multiple variables, values at the same time, seperate assignment by commmas 
# *note* = sign means assignment in python!
x,y,z = 12, 22, 33



