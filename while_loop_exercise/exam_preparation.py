
failed_grades = int(input())

failed_times = 0
decided_tasks = 0
total_grades = 0
last_problem = ''
has_failed = True

while failed_times < failed_grades:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break

    grade = int(input())
    if grade < 4:
        failed_times += 1
    total_grades += grade
    decided_tasks += 1
    last_problem = problem_name
if has_failed:
    print(f'You need a break, {failed_times} poor grades.')
else:
    average_grade = total_grades / decided_tasks
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {decided_tasks}')
    print(f'Last problem: {last_problem}')
