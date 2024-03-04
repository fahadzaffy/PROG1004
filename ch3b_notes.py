
'''
# Topic 1: Special Expressions: 
#      1. Conditional Expression
#           - used to replace simple if else logic with 2 possible values

mark = float(input('Enter your mark: '))
if mark >= 50: print('Pass')
else: print('Fail') 

# can shorten the code 
mark = float(input('Enter your mark: '))
print('Pass' if mark >= 50 else 'Fail')

#     2. Assignment expression
#          - walrus operator:   variable := value #has the lowest priority must use in parentesis to execute
#          - it is an expression not a statement
#          - operator defines variable and initalizes it; returns the value

a, b = 1234, 345233
sum = a+b 
if sum % 7 == 0:
    print('The sum is a multiple of 7 ')
#equivalent to the code block above used to create variables, assign and use the value in an operation
if (total := a + b) % 7 == 0:
    print('The sum is a multiple of 7')

#       Topic 2 - nested decision
#        -if/else in if/else
#       
#        - have if else in if block
#           Example: condition for loan 1) yearly income > 30000 2) working for at least 2 yrs 
'''
income = float(input('Your income: '))
years = int(input('Years you have been wokring: '))
if income > 30000:
    print('Ok income is good')
    if years >= 2: print('Good you are approved')
    else: print('Too short length of employment')

else: print('Your annual income is too low')
#        - have if else in else block


# elif stops when one true condition is met does not execute past the true condition


# Logical operators: 
# used to write complex conditions 
# 3 logical operators: and, or and not

# -1. And operator: only when both conditions are true then the result is true
# -2. Or operator: If one conditoin is true and the other is false then the result is true (only one or other has to be true)
#                  when both connditions in or operator are false then result is false

# -3; not operator (reverse the value): if both values are false then the result is true 

# priorty of operators: not > and > or
# short-circut operation: when we have and operator if the first result is false, then it is not executed past it