hours = int(input())
minutes = int(input()) + 15

minutes_in_hours = 60
hours_in_day = 24

if minutes >= minutes_in_hours:
    minutes = minutes - minutes_in_hours
    hours += 1
if hours >= hours_in_day:
    hours = hours - hours_in_day

if minutes < 10:
    print(f'{hours}:{minutes:02d}')
else:
    print(f'{hours}:{minutes}')


