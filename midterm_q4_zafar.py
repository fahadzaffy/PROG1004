

def get_number(lower=1, upper=20):
    num = int(input('Enter a number between 1 and 20 inclusive: '))
    while num <= lower or num >= upper:
        print('The number is outside of the required range')
        return None
    
    else:
        return num

get_number()
