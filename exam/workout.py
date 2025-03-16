import math
days_workout = int(input())
first_day_km = float(input())

total_km = first_day_km

for km in range(1, days_workout + 1):
    km = int(input())
    first_day_km += first_day_km * ( km / 100)
    total_km += first_day_km

if total_km >= 1000:
    more_km = math.ceil(total_km  - 1000)
    print(f"You've done a great job running {more_km } more kilometers!")
else:
    needed_km = math.ceil(1000 - total_km )
    print(f'Sorry Mrs. Ivanova, you need to run {needed_km} more kilometers')



