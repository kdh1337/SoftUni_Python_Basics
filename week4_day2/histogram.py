n = int(input())

num_under_200 = 0
num_200_399 = 0
num_400_599 = 0
num_600_799 = 0
num_above_or_equal_to_800 = 0

for i in range(1, n+1):
    num = int(input())
    if 0 <= num < 200:
        num_under_200 += 1
    elif 200 <= num <= 399:
        num_200_399 += 1
    elif 400 <= num <= 599:
        num_400_599 += 1
    elif 600 <= num <= 799:
        num_600_799 += 1
    elif num >= 800:
        num_above_or_equal_to_800 += 1

p1 = (num_under_200 / n) * 100
p2 = (num_200_399 / n) * 100
p3 = (num_400_599 / n) * 100
p4 = (num_600_799 / n) * 100
p5 = (num_above_or_equal_to_800 / n) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')