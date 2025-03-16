
player = input()
player_name = ''
player_goals = 0
while player != 'END':

    goals = int(input())

    if goals > player_goals:
        player_goals = goals
        player_name = player

    if goals >= 10:
        break

    player = input()
print(f'{player_name} is the best player!')

if player_goals >= 3:
    print(f'He has scored {player_goals } goals and made a hat-trick !!!')
else:
    print(f'He has scored {player_goals } goals.')





