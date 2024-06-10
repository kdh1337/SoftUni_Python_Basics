trip_price = float(input())
budget = float(input())
action = input()
days = 0
consecutive_days_spending = 0

while budget >= 0:
    amount = float(input())
    days += 1
    if action == 'save':
        budget += amount
        consecutive_days_spending = 0
    elif action == 'spend':
        budget -= amount
        consecutive_days_spending += 1
        if consecutive_days_spending >= 5:
            print("You can't save the money.")
            print(f'{days}')
            break
        if budget < amount:
            budget = 0
    if budget >= trip_price:
        print(f'You saved the money for {days} days.')
        break
    action = input()