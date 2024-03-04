name = input('Enter your name ')
small_pizza = int(input('How many small pizzas? '))
large_pizza = int(input('How many large pizzas? '))
extra_toppings = int(input('How many extra toppings would you like? '))
drinks = int(input('Enter the amounts of drinks '))
total= small_pizza*9.5 + large_pizza*12.99 + extra_toppings*1.49 + drinks*2.23
tax = 0.05
print('Your total before tax is:', total)
print('Your final payment including taxes is:', total * tax + total)
# GOOD JOB!! :) 