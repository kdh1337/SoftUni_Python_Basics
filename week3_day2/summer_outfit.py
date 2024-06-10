temperature = int(input())
time = input()
outfit = 0
shoes = 0

if temperature >= 10 and temperature <= 18:
    if time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    if time == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    if time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

elif temperature > 18 and temperature <= 24:
    if time == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    if time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    if time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

elif temperature >= 25:
    if time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    if time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    if time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")