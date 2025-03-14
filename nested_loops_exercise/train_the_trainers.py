
juries = int(input())

presentation_grade = 0
all_presentations = 0
average_grade = 0



while True:
    command = input()

    if command == 'Finish':
        print(f"Student's final assessment is {average_grade}.")
        break


    for juri in range(juries):
        grades = float(input())
        all_presentations += 1
        presentation_grade += grades

    average_grade = presentation_grade / all_presentations

    presentation_name = input(command)
    for name in range(presentation_name):


    print(f'{average_grade}')





