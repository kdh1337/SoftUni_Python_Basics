month = input()
nights = int(input())
price_studio = 0
price_apart = 0

if month == 'May' or month == 'October':
    price_studio = 50
    price_apart = 65
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apart = 68.70
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apart = 77

if 7 < nights < 14 and (month == 'May' or month == 'October'):
    price_studio = price_studio * 0.95
elif nights > 14 and (month == 'May' or month == 'October'):
    price_studio = price_studio * 0.7
elif nights > 14 and (month == 'June' or month == 'September'):
    price_studio = price_studio * 0.8

if nights > 14:
    price_apart = price_apart * 0.9

total_studio = price_studio * nights
total_apart = price_apart * nights

print(f'Apartment: {total_apart:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')