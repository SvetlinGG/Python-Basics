
days_count = int(input())
total_food = float(input())

biscuits = 0
eated_cat_food = 0
eated_dog_food = 0
eated_total_food = 0

for day in range(1, days_count + 1):
    dog_food = int(input())
    cat_food = int(input())
    if day % 3 == 0:
        eated_dog_food += dog_food
        eated_cat_food += cat_food
        biscuits += (dog_food + cat_food) * 0.1
    else:
        eated_dog_food += dog_food
        eated_cat_food += cat_food
    eated_total_food += dog_food + cat_food



print(f'Total eaten biscuits: {round(biscuits)}gr.')

percent_eated_food = ( eated_total_food / total_food ) * 100
percent_eated_dog_food = ( eated_dog_food / eated_total_food ) * 100
percent_eated_cat_food = ( eated_cat_food / eated_total_food ) * 100
print(f'{percent_eated_food:.2f}% of the food has been eaten.')
print(f'{percent_eated_dog_food:.2f}% eaten from the dog.')
print(f'{percent_eated_cat_food:.2f}% eaten from the cat.')

