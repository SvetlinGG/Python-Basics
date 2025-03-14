

juries = int(input())

total_sum_grades = 0
total_grades_count = 0
result = ''

while True:
    presentation_name = input()
    if presentation_name == 'Finish':
        break

    current_sum_grades = 0

    for _ in range(juries):
        grades = float(input())
        current_sum_grades += grades

    total_sum_grades += current_sum_grades
    total_grades_count += juries
    result += f"{presentation_name} - {current_sum_grades / juries:.2f}.\n"
result += f"Student's final assessment is {total_sum_grades / total_grades_count:.2f}."
print(result)






