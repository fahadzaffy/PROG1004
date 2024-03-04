
def area_perimeter(l,w):
    if l > 0 and w > 0: 
        print(f'The area of the room is: {l*w}')
        print(f'The perimeter of the room is: {(2*l)+(2*w)}')

def messages(x):
    if x > 0:
        for n in range (x):
            print('Hello')

def main():
    l = float(input('L: '))
    w = float(input('W: '))
    area_perimeter(l,w)
    x = int(input('Enter a number: '))
    messages(x)

main()

'''


Write a function print_sequence that takes in two
positional only arguments named start and stop, and one
keyword only arguments named step. The function prints
a number of integers from start to stop with the given
step. By default it will print 1, 2, 3, ..., 100
'''

def print_sequence(start, stop):
    for _ in range(start, stop):
        print('')
