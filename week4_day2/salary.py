open_tabs = int(input())
salary = int(input())

for i in range(1, open_tabs + 1):
    tab = input()
    if salary > 0:
        if tab == 'Facebook':
            salary -= 150
        elif tab == 'Instagram':
            salary -= 100
        elif tab == 'Reddit':
            salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(salary)