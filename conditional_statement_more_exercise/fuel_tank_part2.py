

fuel = input()
fuel_quantity = float(input())
club_card = input()
fuel_price = 0


if fuel_quantity < 20:
    if fuel == 'Gasoline' and club_card == 'Yes':
        fuel_price = fuel_quantity * (2.22 - 0.18)
    elif fuel == 'Diesel' and club_card == 'Yes':
        fuel_price = fuel_quantity * (2.33 - 0.12)
    elif fuel == 'Gas' and club_card == 'Yes':
        fuel_price = fuel_quantity * (0.93 - 0.08)

if fuel_quantity < 20:
    if fuel == 'Gasoline' and club_card == 'No':
        fuel_price = fuel_quantity * 2.22
    elif fuel == 'Diesel' and club_card == 'No':
        fuel_price = fuel_quantity * 2.33
    elif fuel == 'Gas' and club_card == 'No':
        fuel_price = fuel_quantity * 0.93

if fuel_quantity >= 20 or fuel_quantity <= 25:
    if fuel == 'Gasoline' and club_card == 'No':
        fuel_price = (fuel_quantity * 2.22) * 0.92
    elif fuel == 'Diesel' and club_card == 'No':
        fuel_price = (fuel_quantity * 2.33) * 0.92
    elif fuel == 'Gas' and club_card == 'No':
        fuel_price = (fuel_quantity * 0.93) * 0.92

if fuel_quantity >= 20 or fuel_quantity <= 25:
    if fuel == 'Gasoline' and club_card == 'Yes':
        fuel_price = (fuel_quantity * (2.22 - 0.18)) * 0.92
    elif fuel == 'Diesel' and club_card == 'Yes':
        fuel_price = (fuel_quantity * (2.33 - 0.12)) * 0.92
    elif fuel == 'Gas' and club_card == 'Yes':
        fuel_price = (fuel_quantity * (0.93 - 0.08)) * 0.92

if fuel_quantity >= 20 or fuel_quantity <= 25:
    if fuel == 'Gasoline' and club_card == 'No':
        fuel_price = (fuel_quantity * 2.22) * 0.92
    elif fuel == 'Diesel' and club_card == 'No':
        fuel_price = (fuel_quantity * 2.33) * 0.92
    elif fuel == 'Gas' and club_card == 'No':
        fuel_price = (fuel_quantity * 0.93) * 0.92

if fuel_quantity > 25:
    if fuel == 'Gasoline' and club_card == 'Yes':
        fuel_price = (fuel_quantity * (2.22 - 0.18)) * 0.9
    elif fuel == 'Diesel' and club_card == 'Yes':
        fuel_price = (fuel_quantity * (2.33 - 0.12)) * 0.9
    elif fuel == 'Gas' and club_card == 'Yes':
        fuel_price = (fuel_quantity * (0.93 - 0.08)) * 0.9

if fuel_quantity > 25:
    if fuel == 'Gasoline' and club_card == 'No':
        fuel_price = (fuel_quantity * 2.22) * 0.9
    elif fuel == 'Diesel' and club_card == 'No':
        fuel_price = (fuel_quantity * 2.33) * 0.9
    elif fuel == 'Gas' and club_card == 'No':
        fuel_price = (fuel_quantity * 0.93) * 0.9

print(f'{fuel_price:.2f} lv.')