bad_grades_allowed = int(input())
task_name = input()
bad_grades = 0
last_task_name = 0
tasks = 0
total_grades = 0

while task_name != 'Enough':
    grade = int(input())
    last_task_name = task_name
    tasks += 1
    total_grades += grade
    if grade <= 4:
        bad_grades += 1
        if bad_grades >= bad_grades_allowed:
            print(f'You need a break, {bad_grades} poor grades.')
            break
    task_name = input()

if task_name == 'Enough':
    print(f'Average score: {total_grades / tasks:.2f}')
    print(f'Number of problems: {tasks}')
    print(f'Last problem: {last_task_name}')