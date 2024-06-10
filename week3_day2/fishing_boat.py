budget = int(input())
season = input()
fishermen = int(input())
rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fishermen <= 6:
    discount = 0.9
elif fishermen >= 7 and fishermen <= 11:
    discount = 0.85
elif fishermen >= 12:
    discount = 0.75

total_price = rent * discount

if fishermen % 2 == 0 and season != 'Autumn':
    total_price = total_price * 0.95

remaining_money = budget - total_price

if remaining_money >= 0:
    print(f'Yes! You have {remaining_money:.2f} leva left.')
elif remaining_money < 0:
    print(f'Not enough money! You need {abs(remaining_money):.2f} leva.')