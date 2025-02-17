import math
serial_name = input()
time_episode = float(input())
lunch_time = float(input())

lunch = lunch_time * 1/8
relax_time = lunch_time * 1/4

total_lunch_time = lunch + relax_time + time_episode

if lunch_time >= total_lunch_time:
    left_time = math.ceil(lunch_time - total_lunch_time)
    print(f'You have enough time to watch {serial_name} and left with {left_time} minutes free time.')
else:
    needed_time = math.ceil(total_lunch_time - lunch_time)
    print(f"You don't have enough time to watch {serial_name}, you need {needed_time} more minutes.")
