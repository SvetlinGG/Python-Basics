import math

days_count = int(input())
animal_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000

total_needed_food = ( days_count * dog_food ) + ( days_count * cat_food ) + ( days_count * turtle_food)

if total_needed_food <= animal_food:
    left_food = math.floor(animal_food - total_needed_food)
    print(f'{left_food} kilos of food left.')
else:
    needed_food = math.ceil(total_needed_food - animal_food)
    print(f'{needed_food} more kilos of food are needed.')

