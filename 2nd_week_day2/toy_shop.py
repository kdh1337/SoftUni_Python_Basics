puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

trip_price = float(input())
puzzle_number = int(input())
doll_number = int(input())
teddy_bear_number = int(input())
minion_number = int(input())
truck_number = int(input())

sold_toys = puzzle_number + doll_number + teddy_bear_number + minion_number + truck_number

puzzle = puzzle_price * puzzle_number
doll = doll_price * doll_number
teddy_bear = teddy_bear_price * teddy_bear_number
minion = minion_price * minion_number
truck = truck_price * truck_number

sold_toys_price = puzzle + doll + teddy_bear + minion + truck

if sold_toys >= 50:
    sold_toys_price = sold_toys_price - (sold_toys_price * 0.25)

rent = 0.1 * sold_toys_price

profit = sold_toys_price - rent
remaining_money = profit - trip_price

if remaining_money >= 0:
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    print(f'Not enough money! {abs(remaining_money):.2f} lv needed.')

'''
print(sold_toys_price)
print(sold_toys)
print(profit)
print(rent)
print(remaining_money)
'''