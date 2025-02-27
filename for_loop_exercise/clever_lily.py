from math import floor
lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toys = 0
even_age = 0
odd_age = 0
even_half = 0
odd_half = 0

for age in range(1, lily_age + 1):

    if age % 2 == 0:
        even_age = even_age + 10
        even_half += even_age
    else:
        odd_age += 1
        odd_half = odd_age * toy_price

total_money = ( even_half + odd_half ) - floor(age / 2)

if total_money  >= washing_machine_price:
    money_left = total_money - washing_machine_price
    print(f'Yes! {money_left:.2f}')
else:
    money_needed = washing_machine_price - total_money
    print(f'No! {money_needed:.2f}')


