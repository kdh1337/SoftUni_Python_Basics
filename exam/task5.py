daily_goal = int(input())
money_made = 0

while True:

    if money_made >= daily_goal:
        break

    command = input()
    price = 0

    if command == 'closed':
        break

    elif command == 'haircut':
        haircut_type = input()
        if haircut_type == 'mens':
            price = 15
        elif haircut_type == 'ladies':
            price = 20
        elif haircut_type == 'kids':
            price = 10

    elif command == 'color':
        color_type = input()
        if color_type == 'touch up':
            price = 20
        elif color_type == 'full color':
            price = 30

    money_made += price

if money_made >= daily_goal:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {daily_goal - money_made}lv. more.')

print(f'Earned money: {money_made}lv.')