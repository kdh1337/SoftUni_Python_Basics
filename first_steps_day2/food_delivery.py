chicken_menu_orders = int(input())
fish_menu_orders = int(input())
vegan_menu_orders = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery = 2.50

amount_for_menus = (chicken_menu_price * chicken_menu_orders) + (fish_menu_price * fish_menu_orders) + (vegan_menu_price
* vegan_menu_orders)

dessert = amount_for_menus * 0.20

total_order_amount = amount_for_menus + dessert + delivery

print(total_order_amount)