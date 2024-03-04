
x = int(input('Start number: '))
y = int(input('Stop number: '))
print(f'Number\t' f'Squared')
total= 0
for number in range (x,y+1):
    print(number, '\t', (number ** 2))
    total += (number ** 2)
average = total/(y-x+1)
print('Average of squares:', (average))