trip_days = int(input())
room_type = input()
review = input()

nights = trip_days - 1
price = 0
discount = 0
final_price = 0

if room_type == 'room for one person':
    price = 18
    discount = 0

elif room_type == 'apartment':
    price = 25
    if nights < 10:
        discount = 0.3
    elif 10 <= nights <= 15:
        discount = 0.35
    elif nights > 15:
        discount = 0.5

elif room_type == 'president apartment':
    price = 35
    if nights < 10:
        discount = 0.1
    elif 10 <= nights <= 15:
        discount = 0.15
    elif nights > 15:
        discount = 0.20

trip_price = (nights * price) - ((nights * price) * discount)

if review == 'positive':
    final_price = trip_price * 1.25
else:
    final_price = trip_price - (trip_price * 0.1)

print(f'{final_price:.2f}')