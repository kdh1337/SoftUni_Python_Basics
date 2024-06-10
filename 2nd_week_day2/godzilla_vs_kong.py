budget = float(input())
cast = int(input())
clothes_per_member = float(input())

decor_price = 0.1 * budget
clothes_price = clothes_per_member * cast

if cast > 150:
    clothes_price = clothes_price - (clothes_price * 0.1)

remaining_money = budget - (decor_price + clothes_price)

if decor_price + clothes_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(remaining_money):.2f} leva more.")
if decor_price + clothes_price <= budget:
    print("Action!")
    print(f"Wingard starts filming with {abs(remaining_money):.2f} leva left.")

