
budget = float(input())
destination = input()
season = input()
days_count = int(input())

price_for_day = 0

if destination == 'Dubai' and season == 'Winter':
    price_for_day += 45000
elif destination == 'Dubai' and season == 'Summer':
    price_for_day += 40000

if destination == 'Sofia' and season == 'Winter':
    price_for_day += 17000
elif destination == 'Sofia' and season == 'Summer':
    price_for_day += 12500

if destination == 'London' and season == 'Winter':
    price_for_day += 24000
elif destination == 'London' and season == 'Summer':
    price_for_day += 20250

total_price = price_for_day * days_count
if destination == 'Dubai':
    total_price *= 0.7
elif destination == 'Sofia':
    total_price *= 1.25

if budget >= total_price:
    money_left = budget - total_price
    print(f'The budget for the movie is enough! We have {money_left:.2f} leva left!')
else:
    money_needed = total_price - budget
    print(f'The director needs {money_needed:.2f} leva more!')