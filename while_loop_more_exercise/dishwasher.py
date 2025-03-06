
detergent = int(input()) * 750

detergent_for_1_dish  = 5
detergent_for_pots = 15
washed_dishes = 0
washed_pots = 0
loads = 0
while True:

    command = input()
    loads += 1

    if command == 'End':
        break
    dish_count = int(command)
    if loads % 3 == 0:
        washed_pots += dish_count
        detergent -=  dish_count * detergent_for_pots

    else:
        detergent -= (dish_count * detergent_for_1_dish)
        washed_dishes += dish_count
    if detergent < 0:
        print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')

if detergent > 0:
    print(f'Detergent was enough!')
    print(f'{washed_dishes} dishes and {washed_pots} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')
#else:
    #print(f'Not enough detergent, {detergent} ml. more necessary!')



