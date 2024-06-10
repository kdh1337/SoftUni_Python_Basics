family_budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_additional_expenses = int(input())

if nights > 7:
    price_per_night -= price_per_night * 0.05

trip_expenses = nights * price_per_night
additional_expenses = family_budget * percent_additional_expenses / 100
total_expenses = trip_expenses + additional_expenses

if total_expenses <= family_budget:
    print(f'Ivanovi will be left with {family_budget - total_expenses:.2f} leva after vacation.')
else:
    print(f'{total_expenses - family_budget:.2f} leva needed.')