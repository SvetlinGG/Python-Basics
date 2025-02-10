movie_budget = float(input())

statists_count = int(input())
statist_clothes_price = float(input())
clothes_price = statist_clothes_price * statists_count

decor = movie_budget * 0.1
total_money = decor + clothes_price

if statists_count >= 150:
    clothes_price -= (clothes_price * 0.1)
    total_money = decor + clothes_price

if total_money > movie_budget:
    money_needed = total_money - movie_budget
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')

else:
    money_left = movie_budget - total_money
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')


