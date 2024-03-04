
#Write a program to calculate the total payments of movie
#tickets. One ticket is $7.50. If you buy 10 or more, you get
#a 2% discount. If you are a VIP, you get another 10%
#discount. If it is weekend, you get another 5% discount.
#• An example output is as follows (user's input in red):
#Enter number of tickets ($7.50 each, 10+ discount: 2%): 12
#Are you a VIP (VIP disount: 10%) (Y/N): Y
#Is today Saturday or Sunday (Weekend disount: 5%) (Y/N): N
#Total payments: 79.38


price = 7.5
number = int(input('Enter the number of tickets you wish to purchase '))
VIP = input('Are you a VIP (y/n)? ')
weekend_discount = input('Is today a saturday or sunday (y/n)? ')
total = 7.5 * number

if number >= 10:
    discount1 = total * 0.02
else: 
    discount1 = 0

discount2 = 0

if VIP == 'y':
    discount2 = total * 0.1
else:
    discount2 = 0

discount3 = 0

if weekend_discount == 'y':
    discount3 = total * 0.05
else:
    discount3 = 0

print(f'Your total payment is: {total - discount1 - discount2 - discount3:.2f}')