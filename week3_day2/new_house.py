flower = input()
quantity = int(input())
budget = int(input())
price = 0

if flower == 'Roses':
    price = 5
elif flower == 'Dahlias':
    price = 3.80
elif flower == 'Tulips':
    price = 2.80
elif flower == 'Narcissus':
    price = 3
elif flower == 'Gladiolus':
    price = 2.50

if flower == 'Roses' and quantity > 80:
    price = price * 0.9
elif flower == 'Dahlias' and quantity > 90:
    price = price * 0.85
elif flower == 'Tulips' and quantity > 80:
    price = price * 0.85
elif flower == 'Narcissus' and quantity < 120:
    price = price * 1.15
elif flower == 'Gladiolus' and quantity < 80:
    price = price * 1.20

total_cost = price * quantity
remaining_money = budget - total_cost

if remaining_money >= 0:
    print(f'Hey, you have a great garden with {quantity} {flower} and {remaining_money:.2f} leva left.')
elif remaining_money < 0:
    print(f'Not enough money, you need {abs(remaining_money):.2f} leva more.')