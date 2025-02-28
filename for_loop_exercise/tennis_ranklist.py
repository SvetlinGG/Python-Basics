
tournir_count = int(input())
starting_score = int(input())
score_W = 0
score_F = 0
score_SF = 0
tournir_type_W = 0
tournir_type_F = 0
tournir_type_SF = 0
total_score = 0

for _ in range(tournir_count):
    tournir = input()

    if tournir == 'W':
        score_W += 2000
        tournir_type_W += 1
    elif tournir == 'F':
        score_F += 1200
        tournir_type_F += 1
    elif tournir == 'SF':
        score_SF += 720
        tournir_type_SF += 1
total_score = starting_score + score_W + score_F + score_SF
average_score =  ( score_W + score_F + score_SF ) / tournir_count
total_tournirs = tournir_type_W + tournir_type_F + tournir_type_SF
percent_tournir_wins = (tournir_type_W / total_tournirs) * 100
print(f'Final points: {total_score}')
print(f'Average points: {int(average_score)}')
print(f'{percent_tournir_wins:.2f}%')

