
budget = float(input())
nights_count = int(input())
night_price = float(input())
more_money = int(input()) / 100
expensive = budget * more_money

total_price = ( nights_count * night_price ) + expensive

if nights_count >= 7:
    night_price *= 0.95
total_price = ( nights_count * night_price ) + expensive
if budget >= total_price:
    money_left = budget - total_price
    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')
else:
    money_needed = total_price - budget
    print(f'{money_needed:.2f} leva needed.')
