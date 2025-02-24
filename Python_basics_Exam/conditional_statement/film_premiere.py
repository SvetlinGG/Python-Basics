
film_name = input()
packet = input()
ticket_count = int(input())
price = 0

if film_name == 'John Wick' and packet == 'Drink':
    price = ticket_count * 12
elif film_name == 'John Wick' and packet == 'Popcorn':
    price = ticket_count * 15
elif film_name == 'John Wick' and packet == 'Menu':
    price = ticket_count * 19

if film_name == 'Star Wars' and packet == 'Drink':
    price = ticket_count * 18
elif film_name == 'Star Wars' and packet == 'Popcorn':
    price = ticket_count * 25
elif film_name == 'Star Wars' and packet == 'Menu':
    price = ticket_count * 30

if film_name == 'Jumanji' and packet == 'Drink':
    price = ticket_count * 9
elif film_name == 'Jumanji' and packet == 'Popcorn':
    price = ticket_count * 11
elif film_name == 'Jumanji' and packet == 'Menu':
    price = ticket_count * 14

if film_name == 'Star Wars' and ticket_count <= 4:
    price *= 0.7

if film_name == 'Jumanji' and ticket_count == 2:
    price *= 0.85

print(f'Your bill is {price:.2f} leva.')