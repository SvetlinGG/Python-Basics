
needed_money = float(input())
real_money = float(input())

spending_counter = 0
days_counter = 0

while real_money < needed_money and spending_counter < 5:
    operation = input()
    money = float(input())
    days_counter += 1

    if operation == 'spend':
        real_money -= money
        spending_counter += 1
    elif operation == 'save':
        real_money += money
        spending_counter = 0
        if real_money < 0:
            real_money = 0


if spending_counter == 5:
    print("You can't save the money.")
    print(f'{days_counter}')
if real_money >= needed_money:
    print(f'You saved the money for {days_counter} days.')


