budget = float(input())
season = input()
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = 0.30 * budget
        sleep = 'Camp'
    elif season == 'winter':
        price = 0.70 * budget
        sleep = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = 0.40 * budget
        sleep = 'Camp'
    elif season == 'winter':
        price = 0.80 * budget
        sleep = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    price = 0.90 * budget
    sleep = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{sleep} - {price:.2f}')