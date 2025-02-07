LITER_GREEN_PAINT = 3.4
LITER_RED_PAINT = 4.3

x = float(input())  # house_height
y = float(input())  # side_wall_lenght
h = float(input())  # roof_triangle_wall

front_wall_area = x * x
back_wall_area = x * x
door_area = 1.2 * 2
side_wall_area = 2 * (x * y)
window_area = 2 * (1.5 * 1.5)
roof_rect_area = 2 * (x * y)
roof_triangle_area = 2 * (x * h / 2)
walls_area = ((front_wall_area + back_wall_area - door_area)
              + (side_wall_area - window_area))
roof_area = roof_rect_area + roof_triangle_area

needed_liter_green = walls_area / LITER_GREEN_PAINT
needed_liter_red = roof_area / LITER_RED_PAINT

print(f"{needed_liter_green:.2f}")
print(f"{needed_liter_red:.2f}")
