movie_type = input()
rows = int(input())
columns = int(input())
price = 0

total_places = rows * columns

if movie_type == 'Premiere':
    price = total_places * 12
elif movie_type == 'Normal':
    price = total_places * 7.5
elif movie_type == 'Discount':
    price = total_places * 5

print(f'{price:.2f} leva')

