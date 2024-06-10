name = input()
grades = 1
sum_grades = 0
excluded = 0

while grades <= 12:
    grade = float(input())
    if grade < 4.00:
        excluded += 1
        if excluded == 2:
            print(f'{name} has been excluded at {grades} grade')
            break
    else:
        sum_grades += grade
        grades += 1

if excluded < 2:
    average = f'{sum_grades / 12:.2f}'
    print(f'{name} graduated. Average grade: {average}')