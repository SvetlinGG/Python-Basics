
product = input()
city = input()
quantity = float(input())

price = 0

if city == 'Sofia' :
    if product == 'coffee':
        price = quantity * 0.5
    elif product == 'water':
        price = quantity * 0.80
    elif product == 'beer':
        price = quantity * 1.2
    elif product == 'sweets':
        price = quantity * 1.45
    elif product == 'peanuts':
        price = quantity * 1.60
elif city == 'Plovdiv':
    if product == 'coffee':
        price = quantity * 0.4
    elif product == 'water':
        price = quantity * 0.7
    elif product == 'beer':
        price = quantity * 1.15
    elif product == 'sweets':
        price = quantity * 1.3
    elif product == 'peanuts':
        price = quantity * 1.5
elif city == 'Varna':
    if product == 'coffee':
        price = quantity * 0.45
    elif product == 'water':
        price = quantity * 0.7
    elif product == 'beer':
        price = quantity * 1.1
    elif product == 'sweets':
        price = quantity * 1.35
    elif product == 'peanuts':
        price = quantity * 1.55

print(price)