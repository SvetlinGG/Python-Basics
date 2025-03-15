

egg_count_first_player = int(input())
egg_count_second_player = int(input())


while True:

    command = input()


    if command == 'one':
        egg_count_second_player -= 1
        if egg_count_second_player == 0:
            print(f'Player two is out of eggs. Player one has {egg_count_first_player} eggs left.')
            break

    elif command == 'two':
        egg_count_first_player -= 1
        if egg_count_first_player == 0:
            print(f'Player one is out of eggs. Player two has {egg_count_second_player} eggs left.')
            break



    if command == 'End':
        print(f'Player one has {egg_count_first_player} eggs left.')
        print(f'Player two has {egg_count_second_player} eggs left.')
        break






