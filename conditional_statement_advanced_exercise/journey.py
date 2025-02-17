
budget = float(input())
season = input()

destination = ''
place = ''
discount = 1
price_for_pay = 1

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        discount = 0.7
    elif season == 'winter':
        place = 'Hotel'
        discount = 0.3
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        discount = 0.6
    elif season == 'winter':
        place = 'Hotel'
        discount = 0.2
else:
    destination = 'Europe'
    place = 'Hotel'
    discount = 0.1

price_for_pay = budget - ( budget * discount )

print(f'Somewhere in {destination}')
print(f'{place} - {price_for_pay:.2f}')




