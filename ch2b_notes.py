
#review on week 1 
#Announcements
# Tutoring sessions on Friday's 4pm-5pm
#Assignment covers chapter (1-4) use techniques only learned in class

#-intro 
#computer = hardware+software
#CPU = fetch - decode - execute
#machine language is only understood by computers
#assembly languages 
#high level language (compiler based or interpreter based)

#===================================================================================================================================
#Topic 1: Input
#get input from user (keyboard)
#how - fucntion input() will take one argument which is the (promt message), return value will be stored in memory

name = input('What is your name: ') # code will not run next line until user gives valid input
print('Welcome', name, ', are you doing well')
address = input('What is your address? ')
print('Oh living at', address, 'Awesome!')
age_input = input('How old are you?: ')
print('Your age is', age_input, 'Still very young')
print(type(name),type(address),type(age_input))

#anything with fucntion input() will be defaulted to a string
# - we need to convert to different type that we desire (string --> int or float for numbers)
# -- convert fucntions to int int(...)
#-- Convert fucntion to float float(...)

#convert from string to number: int() and float()
age = int(age_input)
print(age, type(age))
# you can combine two steps into one if you already know what value type you want 
#example: if you need a price (flaot) or a integer (number of students) below

price = float(input('What is the price' ))
num_students = int(input('Number of students' ))

print(price, type(price), num_students, type(num_students))

#if conversion is not possible then you will get an error 
#you can convert numbers to string using string() fucntion

#int to convert float 
#float to convert int

a = 32.98  #when converted computer just gets rid of decimal does not round up 
b = int(a)
print('b is', b)

print('Convert a negative int', int(-3.97)) # when using int fucntion to convert float then decimal part is ommitted 


#converting int to float 
print('Convert an int to a float')
#===================================================================================================================================

#Topic 2: Arithmetic

#oprands can be a positive or negative or an intger or float

# - operators = + (addition), -(substraction), *(multiplication)
# - types: both int you get int, mixed you get float

a, b, c = 12, -34, 56
d = a + b
e = b - c
f = a * c
print(a, b, c, d, e, f)
a = 1.23 + 2.34
b = 2.34 - 3.45
c = -33.22 * 22.11

# Next operator is / - division (in this operator result is always a float even if operands are two integers)
a = 12 / 2
b = -34 / 3
c = 123 / 100
d = 12.34 / 234
e = 1234 / -0.1
f = -123.45 / 45.67
print(a, b, c, d, e, f)
# divisor cannot be zero

#Next operator %(remainder), modulus
# - divisor cannot be zero
# what happens if divisor is negative? 

a = 31 % 10 # 31 = 3 * 10 + 1 R 1 
b = 16 % 7 # 16 = 2* 7 + 2 R 2
c = 3.45 % 1.1 

# next operator is exponents represented by **(exponenet)
a = 2 ** 3 # 2 x 2 x 2 (2^3)
b = 2.34 ** -3.45 #can also be a float 
c = 3 ** 0.5 # exponenet that is 0.5 is square root
# [Square root of negative gives "complex"  a=+bi] Out of Scope ((-2) ** 0.5)
print(a, b, c)

a = 3 ** 1 ** 2
print('3 ** 1 ** 2', a)  
# ** is done from right to left if you have multiple exponents together 
# - x ** y ** z = x ** ((y ** z))

# Operator: // (integer division)

a = 13 // 3
b = 123.45 // 1.23
c= -3.453 // 2
print(a, b , c)
#===================================================================================================================================



#==================================================================================================================================
# Chapter 2 b notes 


#Strings and Output

#Announcements : QUIZ 1 on Monday Next week 25 T/F questions 

#REVIEW ON PREVIOUS CLASS: 
# +input, +arithmetic 
#input requires function namede input(promt) "All keyboard inputs are returned as strings"
#to convert from string to number/flaot you need to convert by int(iinput(promt)) or float(input(promt))
#^ above is known as fucntion changing to calling a function within a fucntion to do two things (get input+convert)

#if we want to round decimal places up or down we use fucntion named round() can take 2 arguments round(value, number) by 
#       default number is 0

a = round(56.79)
print(a)
# the number indicates how many decimal points you want if you want an integer leave it as default 
print(round(13.579, 1), round(2523.3232, 3))

#arithmetic 
# - How to use set of operators : + addition, - subtraction, * multiplaction, / division, % modulus, ** exponenet, // integer divsion
# - operands : numbers we can use in operators (can be +/- and int or float)
# - / (division): result is always a float **divisor cannot be zero** 
# - % (remainder): divisor cannot be zero, when divisor is negative 
# - ** (exponenet): when you have multiple exponents do it from right ot left ex: 
#       x ** y ** z = x ** (y**z)
# // (integer divison): you get int divisor cannot be zero example: 10//3 = 3 since its 3.5 we remove the 0.5 to get an int


# Practice Question on Slide 55 
#Write a Python program that asks the user to enter
#the initial velocity and acceleration of an object, and
#the time that has elapsed,
#places them in the variables u, a, and t, and
#prints the final velocity, v, and distance traversed, s,
#using the following equations.

u = float(input('Inital Velocity'))
a = float(input('Acceleration:'))
t = int(input('Time in (seconds)'))

v = u + a * t
s = u * t + 0.5 * a * t ** 2
print('The final velocity is', v)
print('The disctance is', s)


#(Separating Digits in an Integer) Write a program that
#• inputs one five-digit number,
#• separates the number into its individual digits
#• prints the digits separated from one another by three
#spaces each.
#• For example, if the user types in 42139, the program
#should print: 4 2 1 3 9

num = int(input('Give me a five digit integer: '))

#number is 42139
# d5,d4,d3,d1


# how to get last digit is taking remainder of 10 d1 = 
#print(d5, '   ', d4, '   ', d3, '   ', d2, '   ', d1)

d1 = num % 10
d2 = num // 10 % 10
d3 = num // 100 % 10
d4 = num // 1000 % 10
d5 = num // 10000 % 10
print(d5, '   ', d4, '   ', d3, '   ', d2, '   ', d1)