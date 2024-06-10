projection = input()
rows = int(input())
column = int(input())
total_seats = rows * column
income = 0

if projection == 'Premiere':
    income = total_seats * 12
elif projection == 'Normal':
    income = total_seats * 7.50
elif projection == 'Discount':
    income = total_seats * 5.00

print(f'{income:.2f} leva')