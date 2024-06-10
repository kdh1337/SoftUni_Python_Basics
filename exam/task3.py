package_weight = float(input())
service = input()
distance = int(input())
price_per_km = 0
new_price_per_km = 0

if package_weight < 1:
    price_per_km = 0.03
elif 1 <= package_weight < 10:
    price_per_km = 0.05
elif 10 <= package_weight < 40:
    price_per_km = 0.1
elif 40 <= package_weight < 90:
    price_per_km = 0.15
elif 90 <= package_weight < 150:
    price_per_km = 0.2

if service == 'express':
    if package_weight < 1:
        new_price_per_km = 0.8 * price_per_km
    elif 1 <= package_weight < 10:
        new_price_per_km = 0.4 * price_per_km
    elif 10 <= package_weight < 40:
        new_price_per_km = 0.05 * price_per_km
    elif 40 <= package_weight < 90:
        new_price_per_km = 0.02 * price_per_km
    elif 90 <= package_weight < 150:
        new_price_per_km = 0.01 * price_per_km

    surcharge = new_price_per_km * package_weight * distance

else:
    surcharge = 0

final_cost = (price_per_km * distance) + surcharge

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {final_cost:.2f} lv.")