price_per_square_meter_of_nylon = 1.50
price_paint_per_litre = 14.50
price_paint_thinner_per_litre = 5.00

required_nylon = int(input())
required_paint = int(input())
required_thinner = int(input())
hours_labor = int(input())

expenses_materials = ((required_nylon + 2) * price_per_square_meter_of_nylon) + ((required_paint + (required_paint * 0.10))
* price_paint_per_litre) + (required_thinner * price_paint_thinner_per_litre) + 0.40

labor_per_hour_price = expenses_materials * 0.30
total_labor_price = hours_labor * labor_per_hour_price

total_expenses = expenses_materials + total_labor_price

print(total_expenses)

