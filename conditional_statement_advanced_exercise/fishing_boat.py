

budget = int(input())
season = input()
fishman_count = int(input())

price = 0
discount = 1
final_suma = 1
if season == 'Spring':
    if fishman_count <= 6:
        price = 3000
        discount = 0.9
    elif fishman_count <= 11:
        price = 3000
        discount = 0.85
    elif fishman_count > 12:
        price = 3000
        discount = 0.75
elif season == 'Autumn' or season == 'Summer':
    if fishman_count <= 6:
        price = 4200
        discount = 0.9
    elif fishman_count <= 11:
        price = 4200 * 0.85
    elif fishman_count > 12:
        price = 4200 * 0.75
elif season == 'Winter':
    if fishman_count <= 6:
        price = 2600
        discount = 0.9
    elif fishman_count <= 11:
        price = 2600
        discount = 0.85
    elif fishman_count > 12:
        price = 2600
        discount = 0.75

final_suma = price * discount

if season != 'Autumn' and fishman_count % 2 == 0:
    final_suma *= 0.95

if budget >= final_suma:
    money_left = budget - final_suma
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = final_suma - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')