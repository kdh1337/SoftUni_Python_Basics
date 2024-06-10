pack_of_pens_price = 5.80
pack_of_markers_price = 7.20
chemical_per_litre_price = 1.20

number_of_pen_packs = int(input())
number_of_marker_packs = int(input())
litres_of_chemical = int(input())
discount = int(input())

discount_percent = discount / 100

total_amount = float((pack_of_pens_price * number_of_pen_packs) + (pack_of_markers_price * number_of_marker_packs) +
                     (chemical_per_litre_price * litres_of_chemical))

total_amount_after_discount = float(total_amount - (total_amount * discount_percent))

print(total_amount_after_discount)