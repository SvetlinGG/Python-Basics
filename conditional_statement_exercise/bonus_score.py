first_score = int(input())

bonus_score = 0

if first_score <= 100:
    bonus_score = 5
elif first_score <= 1000:
    bonus_score = first_score * 0.2
else:
    bonus_score = first_score * 0.1

if first_score % 2 == 0:
    bonus_score = bonus_score + 1
elif first_score % 5 == 0:
    bonus_score = bonus_score + 2

    print(bonus_score)
    print(first_score + bonus_score)
