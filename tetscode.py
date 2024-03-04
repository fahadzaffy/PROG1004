'''
Write a program to print a step-by-step instructions for
going to our course homepage in SLATE. Write each
step into a function. Write the main function to call these
step functions one by one. Ask the user to press Enter to
display next steps.

def step1():
    print(f'1. Open your Web Browser\n')
    input()
def step2():
    print(f'2. Go to slate.sheridancollege.ca\n')
    input()
step1()
step2()


def steps():
    print('1. Open browser')
    print('2. Go to slate.sheridancollege.ca')
    print('3. Login with your sheridan email')
    print('4. Click on PROG1004')
input('Press Enter to Display Steps: ')  # could have left input() without parameters this 'Pauses' the `program
steps()

print('\n')
def comission():
    sales =float(input('Enter total sales amount: '))
    comission = float(input('Current Commussion Rate: '))
    total_comission = sales * comission
    print(total_comission)
comission()
'''
#this is a test
