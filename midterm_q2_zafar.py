

x = int(input('First integer: '))
y = int(input('Second integer: '))
if x % 2 == 0 and y % 2 ==0:
    print('Both are even')
elif x % 2 == 1 and y % 2 == 1:
    print('Both are odd')
elif x % 2 == 1 and y % 2 == 0:
    print(x, 'is odd', y, 'is even')
else:
  print(x, 'is even', y, 'is odd' )

