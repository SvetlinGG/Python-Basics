
climbers_group = int(input())
top = ''
climbers_musala = 0
climbers_monblan = 0
climbers_kilimanjaro = 0
climbers_k2 = 0
climbers_everest = 0
total_climbers = 0

for _ in range(climbers_group):
    climbers = int(input())
    total_climbers += climbers
    if climbers <= 5:
        climbers_musala += climbers
    elif climbers <= 12:
        climbers_monblan += climbers
    elif climbers <= 25:
        climbers_kilimanjaro += climbers
    elif climbers <=40:
        climbers_k2 += climbers
    elif climbers > 40:
        climbers_everest += climbers

percent_musala = ( climbers_musala / total_climbers ) * 100
percent_monblan = ( climbers_monblan / total_climbers ) * 100
percent_kilimanjaro = ( climbers_kilimanjaro / total_climbers ) * 100
percent_k2 = ( climbers_k2 / total_climbers ) * 100
percent_everest = ( climbers_everest / total_climbers ) * 100
print(f'{percent_musala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kilimanjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')