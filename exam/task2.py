daily_budget = float(input())
daily_revenue = float(input())
total_expenses = float(input())
gift_price = float(input())

days_left = 5

saved_money = days_left * daily_budget
money_earned = days_left * daily_revenue
total_money_saved = saved_money + money_earned
total_profit = total_money_saved - total_expenses

if total_profit >= gift_price:
    print(f'Profit: {total_profit:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {gift_price - total_profit:.2f} BGN.')