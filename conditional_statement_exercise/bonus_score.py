first_score = int(input())

bonus_score = ''

if first_score <=100:
    bonus_score = 5
elif first_score <= 1000:
    bonus_score = first_score * 0.2
else:
    bonus_score = first_score * 0.1

    print()