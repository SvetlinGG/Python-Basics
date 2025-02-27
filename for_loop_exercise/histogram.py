

numbers_count = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for _ in range(numbers_count):
    numbers = int(input())

    if numbers < 200:
        p1 += 1
    elif numbers <= 399:
        p2 += 1
    elif numbers <= 599:
        p3 += 1
    elif numbers <= 799:
        p4 += 1
    elif numbers >= 800:
        p5 += 1
percent_numbers_p1 = ( p1 / numbers_count) * 100
percent_numbers_p2 = ( p2 / numbers_count) * 100
percent_numbers_p3 = ( p3 / numbers_count) * 100
percent_numbers_p4 = ( p4 / numbers_count) * 100
percent_numbers_p5 = ( p5 / numbers_count) * 100

print(f'{percent_numbers_p1:.2f}%')
print(f'{percent_numbers_p2:.2f}%')
print(f'{percent_numbers_p3:.2f}%')
print(f'{percent_numbers_p4:.2f}%')
print(f'{percent_numbers_p5:.2f}%')
