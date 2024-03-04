#Functions 3/3


#Topic 1: math module 
#   -contains code for doing math
#   -constants: pi and e
#   -trigonometric functions: sin, cos, asin, acos, tan #parameters can have to be in radians 
#     degrees (30,45,90,120,360)
#     radians (pi/6,pi/4,pi/2,pi,2pi)
#
# Exponents: pow, exp, log, log10, sqrt

# Rounding: (round), ceil, floor

import math

def math_tester():
    print(f'pi is {math.pi}, and e is {math.e}')
    angle = 90
    # converting degree to radian as trig functions only accept radians***
    print(f'sin of 90 degrees is {math.sin(math.radians(angle))}')
    arc = math.pi / 6
    print(f'sin of pi/6 {math.sin(arc)}')
    #if you need pi or e import math module and use {math.pi} and {math.e}

    a = math.e ** 5
    print(f'log of a is {math.log(a)}')
    b = 1000000
    print(f'log 10 of b is {math.log10(b)}')


    print(f'{math.ceil(1.11)}, {math.ceil(2.99)}')
    print(f'{math.floor(1.11)}, {math.floor(2.99)}')
    print(f'{math.ceil(-1.11)}, {math.ceil(-2.99)}')
    print(f'{math.floor(-1.11)}, {math.floor(-2.99)}')



def main():
    math_tester()

main()

#Topic 2: Modules
#   - a file named somename.py containing code for reusing
#   - module needs to be imported first before use
#   - when imported code in module is executed 
#   - Module can be standalone or import (standalone we run otherwise we just import without running)
#   - # standalone name: if__name__ == '__main__'
#      # by default if there is no imported module the file name is '__main__' otherwise if imported module file name is the file name
      # shape_test()


# MIDTERM REVIEW 25%: 







