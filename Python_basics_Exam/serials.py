
from math import floor





name_of_serial = input()
seasons_count = int(input())
episodes_count = int(input())
time_for_episode = int(input())

episode_plus_advertising = time_for_episode * 1.2

time = episode_plus_advertising * episodes_count
more_episode = (seasons_count * 10 )
total_time = seasons_count * time + more_episode

print(f'Total time needed to watch the {name_of_serial} series is {floor(total_time)} minutes.')

