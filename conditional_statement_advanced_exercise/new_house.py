
flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0
discount = 1

if flowers == 'Roses' and flowers_count > 80:
    price = 5
    discount = 0.9
elif flowers == 'Dahlias' and flowers_count > 90:
    price = 3.8
    discount = 0.85
elif flowers == 'Tulips' and flowers_count > 80:
    price = 2.8
    discount = 0.85
elif flowers == 'Narcissus' and flowers_count < 120:
    price = 3
    discount = 1.15
elif flowers == 'Gladiolus' and flowers_count < 80:
    price =  2.5
    discount = 1.2


final_sum = ( flowers_count * price ) * discount

if budget >= final_sum:
    money_left = budget - final_sum
    print(f'Hey, you have a great garden with {flowers_count} {flowers} and {money_left:.2f} leva left.')
else:
    money_needed = final_sum  - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')

