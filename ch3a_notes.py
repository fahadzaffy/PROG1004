# DECISION STRUCTURES AND BOOLEAN LOGIC

# Topic 1 - Control Structures 

# 1.) Sequence: write first and runs first or in sequence 

# 2.) Decision (aka selection): 
#       -Based on a condition, decides to do or not to do 

#       -Single Alternative: (One way selection)
#           - ex: if it is raining, then bring raincoat

#       -Dual Alternative: (two-way selection)
#           - EX: if raining, raincoat, otherwise, sunglasses


#       -Multiple Selection (match-case, out-of-scope)


# 3.) Repetiton (Iteration, Loop); ch4, 3 classes
#      - Based on condition does something repeatedly 


# +TOPIC 2 - CONDITION 
#               -Boolean Expression: Has 2 possible values either True or False.
#               -SIX RELATION OPERATORS (COMPARISION)
#               - >: greater than and >= greater than or equal to
#               - <: , <= less than, or less than or equal to
#               - == (Equal to),  != (not equal to)
x, y = True, False
print(x, y, type(x), type(y))  #True False <class 'bool'> <class 'bool'>

a1 = 12 > 23  #false
b1 = 34.45 >= 23.34 #true
print(a1, b1)

a2, b2 = 234 < 202, 2345 <= 2345  #Flase, True
print(a2,b2)

a3, b3 = 1234 == 234, 234 != 234  #False, False
print(a3,b3)  

#when coparing two + values it results in a condition or boolean expression

# string comparison: 
#                   - Each character in a string has a number  (ASCII code)
#                   - 'Welcome' vs. 'WelcoMe': find the first different character in sequencee and then compare ASCII codee
#                          Compares 'm' to 'M' (109 to 77) ----> m>M resulting in welcome > welcoMe 

s1, s2 = 'welcome', 'welcoMe'
print(s1 < s2) # m > M 


#  + Topic 3 - Single Alternative (One-way selection): if statement 
#               Syntax: if header/clasue + if body/block
#                       if condition: 
#                               statement 1   #makes sure to indent if blocks for one level
#                               statement 2   #one block has one statement, write it in one line (used for short conditoins)
#
#               Logic: When condition is true, then we will run code block otherwise ignored


weather = input('What is the weather like?: ')
if weather == 'raining':
    print('Bring an umbrella')

print('Have a good day')


guest = input('What is your name: ')
age = int(input('What is your age: '))
print(f'Hi, {guest}, welcome, have a drink')
if age < 19:
    print('Oh, you are still young, have some water')


#    Topic 4: Dual Alternative (two way selection): if/else statement
#               - syntax: 
#                   if condition: 
#                           statements 
#                   else: 
#                           statements 
# 
# Logic: when condition is true run block, otherwise run else block 
    
mark = float(input('What is your mark?: '))
if mark >= 50: 
    print('Congrats, you passed!')

else: 
    print('Unfortunately, you have failed')  


# read two integers, print if the first one is a multiple of the second one 
    
num1=int(input('First Number: '))
num2=int(input('Second Number: '))
if num1 % num2 == 0:   # if the remainder or is 0 logically that means the numbers being compared are factors of each other
    print(f'{num1} is a multiple of {num2}')

else:
    print(f'{num1} is not a multiple of {num2}')    