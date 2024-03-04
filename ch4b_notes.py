# repetition 2/3

# Topic 1 - Augumented assignment
# -update variable with new value by doing something to variable itself
# operators: (+), (-), (*), (/), (%), (**), (//)
a = 10
a = a +1 # take original value add one and assign back to variable
a += 1 # += is agumented assignment operator

b = 12
b = b -2
b -= 2 # used to update variable other agumnetative assignments: 
# b *= 3 same as b = b * 3

# (+=), (-=), (*=), (/=), (%=), (**=), (//=) [No spaces in between]

#Topic 2 : Running Total
#          Define an accumulator variable, initalized to 0
#  
# what is the sum or 1, 2, 3...., 100

sum = 0 # is our accumilator
for x in range (1,101): # x will be 1, 2, 3.... 100
    sum += x  #same as 1+2+3 adding x to itself everytime value changes
    print(f'sum of 1 to 100 is {sum}')

# Topic 3 - Sentinel 
# - a signal that marks the end of a sequence of data 
# - a special value to tell program that there is no more data 
# - Example: mark(-1), name($)




# Topic 4: Input validation 
# garbage in --> garbage out 
# - use a while loop

# Example: read age (18, 60), if not valid then repromt until valid