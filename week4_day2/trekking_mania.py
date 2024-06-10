groups = int(input())

group_5_people = 0
group_6_12_people = 0
group_13_25_people = 0
group_26_40_people = 0
group_41_more_people = 0
total_people = 0

for i in range(1, groups + 1):
    num = int(input())
    total_people += num
    if 0 <= num <= 5:
        group_5_people += num
    elif 6 <= num <= 12:
        group_6_12_people += num
    elif 13 <= num <= 25:
        group_13_25_people += num
    elif 26 <= num <= 40:
        group_26_40_people += num
    elif num >= 41:
        group_41_more_people += num

p1 = group_5_people / total_people * 100
p2 = group_6_12_people / total_people * 100
p3 = group_13_25_people / total_people * 100
p4 = group_26_40_people / total_people * 100
p5 = group_41_more_people / total_people * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')