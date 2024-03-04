
ticket_price = 11.99
discount = 0.05
print('Price for one ticket:', ticket_price)
tickets_purchased = int(input('Number of Tickets: '))
total = total = tickets_purchased * ticket_price
if tickets_purchased >= 10:
    print(f'10 or more tickets, 5% discount'
          f'\nTotal Cost: {total - (total * discount):.2f}')
else:
    print(f'Less than 10 tickets no discount'
          f'\n Total Cost: {total:.2f}')