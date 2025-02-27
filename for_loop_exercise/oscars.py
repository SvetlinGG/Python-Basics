
actor_name = input()
beginner_score = float(input())
jourie = int(input())
total_score = beginner_score

for _ in range(0, jourie):
    name_joury = input()
    score_joury = float(input())

    total_score += ( len(name_joury)) * ( score_joury/2 )

    if total_score > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_score:.1f}!')
        break
else:
    needed_score = 1250.5 - total_score
    print(f'Sorry, {actor_name} you need {needed_score:.1f} more!')
