'''
balance = 0
more_money = input('More money? (y-yes): ')
while more_money == 'y':
    amount = float(input('How much to deposit? '))
    balance += amount
    more_money = input('More money? (y-yes): ')
    print(balance)
'''

# read radius, print area, until radius is -1 (means no more circle)
'''
radius = float(input('Enter the radius (-1 to stop): '))
while radius != -1: 
    print(3.14 * radius ** 2)
    radius = float(input('Enter the radius (-1 to stop): '))
'''
# Example: read age (18, 60), if not valid then repromt until valid
    
'''age = int(input('Enter your age: '))
while age < 18 or age > 60: 
    print('Error: Age must be 18 - 60')
    age = int(input('Enter your age: '))
print ('A valid age:', age)
'''
# Example: read colour (red, green, yellow) validate it
# print message when valid

'''color = input('Traffic light color: ')
while color != 'red' and color != 'green' and color != 'yellow':
    print('Invalid color')
    color = input('Traffic light color: ')
    
    print('Stop' if color == 'red' else 
          'lets go' if color == 'green'
          else 'be careful')'''

name = input('Enter your name (type stop to quit): ')
while name != 'stop':

    course_1 = int(input('Enter your mark for the first course: '))
    while course_1 < 0 or course_1 > 100: 
        print('Error: not a valid mark')
        course_1 = int(input('Enter your mark for the first course: '))

    course_2 = int(input('Enter your mark for the second course: '))

    while course_2 < 0 or course_2 > 100: 
        print('Error: not a valid mark')
        course_2 = int(input('Enter your mark for the second course: '))

    course_3 = int(input('Enter your mark for the third course: '))

    while course_3 < 0 or course_3 > 100: 
        print('Error: not a valid mark')
        course_3 = int(input('Enter your mark for the third course: '))

    course_4 = int(input('Enter your mark for the fourth course: '))

    while course_4 < 0 or course_4 > 100: 
        print('Error: not a valid mark')
        course_4 = int(input('Enter your mark for the fourth course: '))
        
    course_5 = int(input('Enter your mark for the fifth course: '))

    while course_5 < 0 or course_5 > 100: 
        print('Error: not a valid mark')
        course_5 = int(input('Enter your mark for the fifth course: '))
        
    total = course_1 + course_2 + course_3 + course_4 + course_5
    print(f'{name}, your average is: {total / 5} ')
    name = input('Enter your name (type stop to quit): ')

