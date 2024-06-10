def calculate_delivery_cost(weight, service_type, distance):
    # Начални условия за цени на километър
    if weight < 1:
        cost_per_km = 0.03
    elif 1 <= weight < 10:
        cost_per_km = 0.05
    elif 10 <= weight < 40:
        cost_per_km = 0.10
    elif 40 <= weight < 90:
        cost_per_km = 0.15
    elif 90 <= weight <= 150:
        cost_per_km = 0.20

    # Изчисляване на надценка за всеки килограм за услуга "express"
    if service_type == "express":
        if weight < 1:
            markup_per_kg = 0.8 * cost_per_km
        elif 1 <= weight < 10:
            markup_per_kg = 0.4 * cost_per_km
        elif 10 <= weight < 40:
            markup_per_kg = 0.05 * cost_per_km
        elif 40 <= weight < 90:
            markup_per_kg = 0.02 * cost_per_km
        elif 90 <= weight <= 150:
            markup_per_kg = 0.01 * cost_per_km

        # Изчисляваме надценката за теглото
        express_surcharge = markup_per_kg * weight * distance
    else:
        # Няма надценка за "standard" услуга
        express_surcharge = 0

    # Изчисляваме крайната цена на доставката
    final_cost = (cost_per_km * distance) + express_surcharge

    return final_cost


# Четем входните данни
weight = float(input("Enter the weight of the shipment in kg: "))
service_type = input("Enter the type of service ('standard' or 'express'): ").strip().lower()
distance = int(input("Enter the distance in km: "))

# Изчисляваме крайната цена
cost = calculate_delivery_cost(weight, service_type, distance)

# Извеждаме крайния резултат с подходящо закръгляне
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {cost:.2f} lv.")
