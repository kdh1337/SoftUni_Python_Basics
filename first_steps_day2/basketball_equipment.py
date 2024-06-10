annual_tax = int(input())

shoes_price = annual_tax - (annual_tax * 0.40)
uniform_price = shoes_price - (shoes_price * 0.20)
basketball_price = 0.25 * uniform_price
accessories_price = 0.2 * basketball_price

total_amount = annual_tax + shoes_price + uniform_price + basketball_price + accessories_price

print(total_amount)