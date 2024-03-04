'''
print('Hello World 1')
print('Hello World 2')

print('Hello everyone!,\nHow is it going today? \nThis is going to be another new line')


print('I\'m in \"Love\" with \'Python\'')  #slashes are ignored? How to add slashes in print function? 

print('I\'m in love with python and I love the seperator \\\\\\') #seperator \ prints what ever character is in followed 

print('Jack' + 'Anna')


a = 13 // 3
b = 27 // 4
c= 50 // 4
print(a, b , c)
'''

# Page 41 Exercise:

'''Write a program that
• Prompts the user for an integer
• Displays if it is positive or negative or zero
– If it is positive, displays if it is less than 50, 50,
between 51 and 84, 85, or greater than 85

– If it is negative, displays if it is even or odd
• Checks whether it is
– divisible by 2 and 3,
– divisible by 2 or 3 but not both, or
– Not divisible by either 2 or 3

number = int(input('Enter an interger: '))
if number > 0: print(f'The number {number} is positive')
if number <0: print(f'The number {number} is negative')
if number <0 and number % 2 == 0: print(f'The number {number} is even')
elif number<0 and number % 2 != 0: print(f'The number {number} is odd')
elif number == 0: print(f'The number is zero')
elif number == 85: print(f'The number {number} is equal to 85')
elif number > 85: print(f'The number {number} is greater than 85')
elif number == 50: print(f'The number {number} is equal to 50')
elif number < 50: print(f'The number {number} is less than 50')
elif number > 51 and number <84: print(f'The number {number} is between 51 and 84')
'''


# Exercise page 59:

'''
Write a program that reads three integers, sorts and
displays the numbers in an increasing order

'''
'''
x = int(input('Give me the first number: '))
y = int(input('Give me the second number: '))
z = int(input('Give me the third number: '))

if x < y < z : print(x, y , z)
elif x < z < y: print(x, z, y)
elif y < x < z: print (y, x, z)
elif y < z < x: print(y, z, x)
elif z < y < x: print(z, y, x)
elif z < x < y: print(z, x, y)
'''


'''Read int radius and calculate the area of a circle, until the
radius input is -1'''
'''
#1
count = 0
while count >= -1: 
    radius = float(input('What is the radius: '))
    print('The area of the circle is: ', (radius * radius * 3.14))    
    count = radius - 1
'''
'''Ask the user to enter the number of circles, then read the
radius and print the area and perimeter for each circle

#2 



run_again = True
circles = int(input('How many circles: '))
radius = float(input('What is the radius: '))
print(f'The area of the circle is: {radius * radius * 3.14} and the perimeter is: {2 * 3.14 * radius}')
answer = input('Do you more circles? (y-Yes, others-No)')
if answer != 'y': run_again = False
'''

'''
# exercise on slide 25 and do others at home, please:

for n in range (1,101):
    print(n, end = ' ')

print('\n')

for n in range (1, 101):
    if n % 2 == 0:
        print(n, end = ' ')

print('\n')

for n in range (1,101):
    if n % 2 != 0:
        print(n, end = ' ')

print('\n')

for n in range (1,101):
    if n % 7 == 0: 
        print(n, end = ' ')


print('\n')

for n in range (1, 100, 3):
    print(n+1, end = ' ')

print('\n')

for n in range (10,100, 11):
    print(n+1, end = ' ')
'''

'''
read a positive integer, compute and prints its
factors, determine whether it is a prime number.

factor =  suppose x is divisible by y then y is a factor of x
prime number can be divided by itself and 1 
'''


'''
#version 1: 
num = int(input('Enter a positive integer: '))
n = 1
count = 0
while n <= num: 
    if num % n == 0:
        print(n, end =' ')
        count = count +1
    if count == 2 : print(f'{num} is a prime number')
    else: print(f'{num} is not a prime number')
    n = n + 1
'''


'''
print('\n')

num = int(input('Enter a positive integer: '))
count = 0
for n in range (1, num + 1):
    if num % n == 0:
        print (n, end = '')
        count = count + 1
if count == 2: print(f'{num} is a prime number')
else: print(f'{num} is not a prime number')
'''

sum = 0
for x in range (2, 100): 
    sum += x
    if x % 2 == 0: 
        print (sum)
    

# this is a test