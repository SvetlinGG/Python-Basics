from conditional_statement_advanced_lab.small_shop import quantity

fruit = input()
week_day = input()
quantity = float(input())
price = 0


if week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'banana':
        price = 2.5
elif week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'apple':
        price = 1.2
elif week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'orange':
        price = 0.85
elif week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'grapefruit':
        price = 1.45
elif week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'kiwi':
        price = 2.7
elif week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'pineapple':
        price = 5.5
elif week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'grapes':
        price = 3.85


if week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'banana':
        price = 2.7
elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'apple':
        price = 1.25
elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'orange':
        price = 0.9
elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'grapefruit':
        price = 1.6
elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'kiwi':
        price = 3.00
elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'pineapple':
        price = 5.6
elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'grapes':
        price = 4.2

if price:
    total = price * quantity
    print(f'{total:.2f}')
else:
    print('error')