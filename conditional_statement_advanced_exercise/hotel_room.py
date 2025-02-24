month = input()
days_stay = int(input())

price_apartment = 0.0
price_studio = 0.0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
elif month == "June" or month == "September":
    price_studio = 75.2
    price_apartment = 68.7
if month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

if (month == "May" or month == "October") and (14 < days_stay):
    price_studio = (price_studio - (price_studio * 0.30))
elif (month == "May" or month == "October") and (7 < days_stay):
    price_studio = (price_studio - (price_studio * 0.05))

if (month == "June" or month == "September") and (14 < days_stay):
    price_studio = (price_studio - (price_studio * 0.20))

if days_stay > 14:
    price_apartment = (price_apartment - (price_apartment * 0.10))

print(f"Apartment: {price_apartment * days_stay:.2f} lv.")
print(f"Studio: {price_studio * days_stay:.2f} lv.")