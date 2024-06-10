age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

money_from_gifts = 0
toys = 0
brother_steal = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_from_gifts += (10 * i) / 2
        brother_steal += 1
    else:
        toys += 1

money_from_toys = toys * price_per_toy
after_steal_money = money_from_gifts - brother_steal
total_money = money_from_toys + after_steal_money

difference = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')