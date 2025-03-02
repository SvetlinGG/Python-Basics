
student_name = input()

total_grades = 0
failed_years = 0
years_counter = 1

while True:
    grades = float(input())

    if grades < 4:
        failed_years += 1
        if failed_years > 1:
            failed_years = years_counter + 1
            print(f'{student_name} has been excluded at {years_counter} grade')
            break
        continue


    years_counter += 1
    total_grades += grades

else:
    average_grade = total_grades / 12
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')







