import math
world_record = float(input())

distance_in_meters = float(input())
time_for_one_meter = float(input())

delay = math.floor(distance_in_meters / 15) * 12.5

time_for_distance = (distance_in_meters  * time_for_one_meter) + delay

if world_record > time_for_distance:
    print(f'Yes, he succeeded! The new world record is {time_for_distance:.2f} seconds.')
elif world_record <= time_for_distance:
    needed_time = time_for_distance - world_record
    print(f'No, he failed! He was {needed_time:.2f} seconds slower.')

