
film_name = input()
hall_type = input()
tickets_count = int(input())

income = 0

if film_name == 'A Star Is Born' and hall_type == 'normal':
    income = tickets_count * 7.5
elif film_name == 'A Star Is Born' and hall_type == 'luxury':
    income = tickets_count * 10.5
elif film_name == 'A Star Is Born' and hall_type == 'ultra luxury':
    income = tickets_count * 13.5

if film_name == 'Bohemian Rhapsody' and hall_type == 'normal':
    income = tickets_count * 7.35
elif film_name == 'Bohemian Rhapsody' and hall_type == 'luxury':
    income = tickets_count * 9.45
elif film_name == 'Bohemian Rhapsody' and hall_type == 'ultra luxury':
    income = tickets_count * 12.75

if film_name == 'Green Book' and hall_type == 'normal':
    income = tickets_count * 8.15
elif film_name == 'Green Book' and hall_type == 'luxury':
    income = tickets_count * 10.25
elif film_name == 'Green Book' and hall_type == 'ultra luxury':
    income = tickets_count * 13.25

if film_name == 'The Favourite' and hall_type == 'normal':
    income = tickets_count * 8.75
elif film_name == 'The Favourite' and hall_type == 'luxury':
    income = tickets_count * 11.55
elif film_name == 'The Favourite' and hall_type == 'ultra luxury':
    income = tickets_count * 13.95

print(f'{film_name} -> {income:.2f} lv.')