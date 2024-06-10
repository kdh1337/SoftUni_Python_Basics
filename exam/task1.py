percent_fat = int(input())
percent_protein = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

fat_total = (percent_fat / 100) * total_calories / 9
protein_total = (percent_protein / 100) * total_calories / 4
carbs_total = (percent_carbs / 100) * total_calories / 4

food_weight = fat_total + protein_total + carbs_total
calories_for_gram = total_calories / food_weight
not_water_amount = 100 - percent_water
gram = not_water_amount / 100 * calories_for_gram

print(f'{gram:.4f}')