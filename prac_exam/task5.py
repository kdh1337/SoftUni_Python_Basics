budget = float(input())
products_purchased = 0
purchase_price = 0
third_product_count = 0

while True:
    product = input()

    if product == 'Stop':
        print(f'You bought {products_purchased} products for {purchase_price:.2f} leva.')
        break

    product_price = float(input())
    third_product_count += 1

    if third_product_count == 3:
        product_price = product_price / 2
        third_product_count = 0

    if budget < product_price:
        print(f"You don't have enough money!")
        print(f'You need {product_price - budget:.2f} leva!')
        break

    budget -= product_price
    purchase_price += product_price
    products_purchased += 1