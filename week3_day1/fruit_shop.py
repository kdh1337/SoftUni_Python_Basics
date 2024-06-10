fruit = input()
day = input()
quantity = float(input())
price = 0
valid_day = (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'
             or day == 'Saturday' or day == 'Sunday')
valid_fruit = (fruit == 'banana' or fruit == 'apple' or fruit == 'orange' or fruit == 'grapefruit' or fruit == 'kiwi'
               or fruit == 'pineapple' or fruit == 'grapes')

if not valid_day:
    print('error')
elif not valid_fruit:
    print('error')

elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = 2.50
    if fruit == 'apple':
        price = 1.20
    if fruit == 'orange':
        price = 0.85
    if fruit == 'grapefruit':
        price = 1.45
    if fruit == 'kiwi':
        price = 2.70
    if fruit == 'pineapple':
        price = 5.50
    if fruit == 'grapes':
        price = 3.85
    print(f'{price * quantity:.2f}')

elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    if fruit == 'apple':
        price = 1.25
    if fruit == 'orange':
        price = 0.90
    if fruit == 'grapefruit':
        price = 1.60
    if fruit == 'kiwi':
        price = 3.00
    if fruit == 'pineapple':
        price = 5.60
    if fruit == 'grapes':
        price = 4.20
    print(f'{price * quantity:.2f}')