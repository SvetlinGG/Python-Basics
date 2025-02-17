
flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0

if flowers == 'Roses' and flowers_count > 80:
    price = ( flowers_count * 5 ) * 0.9
elif flowers == 'Dahlias' and flowers_count > 90:
    price = (flowers_count * 3.8) * 0.85
elif flowers == 'Tulips' and flowers_count > 80:
    price = (flowers_count * 2.8) * 0.85
elif flowers == 'Narcissus' and flowers_count < 120:
    price = (flowers_count * 3) * 1.15
elif flowers == 'Gladiolus' and flowers_count < 80:
    price = (flowers_count * 2.5) * 1.2




if budget >= price:
    money_left = budget - price
    print(f'Hey, you have a great garden with {flowers_count} {flowers} and {money_left:.2f} leva left.')
else:
    money_needed = price  - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')

