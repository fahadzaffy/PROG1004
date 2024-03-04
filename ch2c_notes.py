#Topic 1: Programming Styles:
#       - Commenting, Naming, Spacing, Line Length 

#Commenting: (Documentation) help reader understand the code
# Heading comments: exlpain the code or give you an abstract understanding of the prgoram
# (name, author, version, date, description)

#Internal Comment are (added on top of code segment or code block)
#   or somewhere where the logic is complicated (explaining logic)
#   One-line comment (usually on top of the statement), or in-line comment ---> added in the same line as statements if short

# Naming: variables must have a meaningful name(self documentation), follow a style (preferred snake_case)

#spacing: 
# - one space before and after operator a = 321 + 213 - 345 * 897 / 123.5
# and one space after a comma
# no space in fucntion name and () fucntions needs to take argument f(x)
# no space inside parentesis at the beginnning/end of the brackets 
# indentation: (doubles as style and part of your code) gives error if not correctly indented (four spaces)

#Line length:
#   - keep all the lines in 80 characters (coloumn width)
# to seperate a long line into multiline: add \
# Good practice to seperate infront of operator with backslash "\"
# anything inside parentesis, no backslash is needed





# Topic 2: String Concatnation
# automatically concatonates automatically if you have two strings next to each other(implicit concatnation)
# for numbers you need to convert to strings to concatnate 
#name = 'Jack'
#print('Hello', + name' + 'How are you')


# Topic 3: Print()
# -ending: by default is a new line, change using end ='...'
print('Hello Everyone!')
print('How is it going today?')

print('Hello everyone!', end=' ')
print('How is it going today?')

# to print multiple values seperator by default is an invisible space, change using sep-='...'

country = 1
city = 905
number = 8960-817

print(country, city, number, sep='-')

# escape(\?): new line (\n) if you want to print on multiple (new lines) instead of using multiple print functions 
# tab(\t), '(\), (\\)

print('Hello everyone!,\nHow is it going today?')

# f-string : 
# a string prefixed with a f (means formation string)
# - can have place holders {....}, can be a value, expression or variable

message = f'Hello World'
name = 'Jack Alex'
age = 19
score = 8.2359252

print(f'My name is {name}, I am {age}, the score I have is {score}')

# f-string functions: 
#     string alighnment (< ^ >) and width 
#     integers: alighnment and width, comma-sepereated 3-digits, percentage
#     float numbers: alighnement, width, comma-seperated, percentage and precision

print(f'My name is {name: <30}') #is aligned to the left 
print(f'My name is {name: ^30}') #is aligned to the center
print(f'My name is {name: >30}') #is alighned to the right

print(f'The number is {65789749141:,d}') #3 digit seperate, d - integer

print(f'The number is {65789749141:^25,d}')

print(f'The percentage is {23: %}')


salary = 35781641.2314
print(f'My salary is {salary: ,.2f}') # : colon means formatting .2f means to keep two digits, f means float, also rounds
#floats can be printed in e - in scientific notation if you change .2f to .2e