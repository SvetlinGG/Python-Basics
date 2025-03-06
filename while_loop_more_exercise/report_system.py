current_money = int(input())
total_money = 0
card_payment = 0
cash_payment = 0
payment_type = 0
card = 0
cash = 0

command = input()

while command != 'End':
    payment_type +=1

    product = int(command)

    if product > 100 and payment_type % 2 != 0 or product <= 10 and payment_type % 2 == 0:
        print('Error in transaction!')


    elif product <= 100 and payment_type % 2 != 0:
            cash_payment += product
            cash += 1
            print('Product sold!')
    elif product > 10 and payment_type % 2 == 0:
            card_payment += product
            card += 1
            print('Product sold!')

    total_money = card_payment + cash_payment
    if total_money >= current_money:
        print(f'Average CS: {cash_payment / cash:.2f}')
        print(f'Average CC: {card_payment / card:.2f}')
        break

    command = input()
else:
    print('Failed to collect required money for charity.')


