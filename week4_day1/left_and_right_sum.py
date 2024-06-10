n = int(input())
left_total = 0
right_total = 0

for i in range(1, n+1):
    left_total += int(input())

for i in range(1, n+1):
    right_total += int(input())

if left_total == right_total:
    print(f'Yes, sum = {left_total}')
else:
    print(f'No, diff = {abs(left_total - right_total)}')