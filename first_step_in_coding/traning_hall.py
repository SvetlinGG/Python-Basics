import math

w = float(input())
h = float(input()) - 1

work_space = math.ceil(0.7 * 1.2)
working_rows = math.floor(w / 1.2)

working_columns = math.floor(h / 0.7)
total_work_places = (working_rows * working_columns) - ( 3 * work_space)

print(total_work_places)
















