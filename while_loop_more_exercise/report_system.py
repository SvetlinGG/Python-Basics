# current_money = int(input())
# total_money = 0
# card_payment = 0
# cash_payment = 0
# payment_type = 0
# card = 0
# cash = 0
#
# command = input()
#
# while command != 'End':
#     payment_type +=1
#
#     product = int(command)
#
#     if product > 100 and payment_type % 2 != 0 or product <= 10 and payment_type % 2 == 0:
#         print('Error in transaction!')
#
#
#     elif product <= 100 and payment_type % 2 != 0:
#             cash_payment += product
#             cash += 1
#             print('Product sold!')
#     elif product > 10 and payment_type % 2 == 0:
#             card_payment += product
#             card += 1
#             print('Product sold!')
#
#     total_money = card_payment + cash_payment
#     if total_money >= current_money:
#         print(f'Average CS: {cash_payment / cash:.2f}')
#         print(f'Average CC: {card_payment / card:.2f}')
#         break
#
#     command = input()
# else:
#     print('Failed to collect required money for charity.')
#



expected_sum = int(input())

total_pay = \
    cash_pay = \
    people_cash = \
    card_pay = \
    people_card = \
    cycle = 0
is_collected = False

while total_pay < expected_sum:
    command = input()
    cycle += 1

    if command == "End":
        is_collected = True
        print("Failed to collect required money for charity.")
        break

    command = int(command)


    if command > 100 and cycle % 2 != 0 or command <= 10 and cycle % 2 == 0:
        print("Error in transaction!")


    elif command <= 100 and cycle % 2 != 0:
        cash_pay += command
        people_cash += 1
        print("Product sold!")

    elif command > 10 and cycle % 2 == 0:
        card_pay += command
        people_card += 1
        print("Product sold!")

    total_pay = cash_pay + card_pay
    if total_pay >= expected_sum:
        print(f"Average CS: {cash_pay / people_cash:.2f}\nAverage CC: {card_pay / people_card:.2f}")
