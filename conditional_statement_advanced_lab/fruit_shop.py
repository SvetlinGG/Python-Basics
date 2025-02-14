from conditional_statement_advanced_lab.small_shop import quantity

fruit = input()
week_day = input()
quantity = float(input())
price = 0


if week_day == 'Monday' and week_day == 'Tuesday' and week_day == 'Wednesday' and week_day == 'Thursday' and week_day == 'Friday':
    if fruit == 'banana':
        price = quantity * 2.5
    elif fruit == 'apple':
        price = quantity * 1.2
    elif fruit == 'orange':
        price = quantity * 0.85
    elif fruit == 'grapefruit':
        price = quantity * 1.45
    elif fruit == 'kiwi':
        price = quantity * 2.7
    elif fruit == 'pineapple':
        price = quantity * 5.5
    elif fruit == 'grapes':
        price = quantity * 3.85
elif week_day == 'Saturday' and week_day == 'Sunday':
    if fruit == 'banana':
        price = quantity * 2.7
    elif fruit == 'apple':
        price = quantity * 1.25
    elif fruit == 'orange':
        price = quantity * 0.9
    elif fruit == 'grapefruit':
        price = quantity * 1.6
    elif fruit == 'kiwi':
        price = quantity * 3.00
    elif fruit == 'pineapple':
        price = quantity * 5.6
    elif fruit == 'grapes':
        price = quantity * 4.2
print(f'{price:.2f}')