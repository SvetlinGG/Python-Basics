free_days_count = int(input())

working_days = 365 - free_days_count
play_in_work_days = working_days * 63

play_in_free_days = free_days_count * 127

total_time = play_in_work_days + play_in_free_days

if total_time >= 30000:
    print('Tom will run away')
    hours = (total_time - 30000) // 60
    minutes = (total_time - 30000) % 60
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    hours = ( 30000 - total_time) // 60
    minutes = ( 30000 - total_time) % 60
    print(f'{hours} hours and {minutes} minutes less for play')