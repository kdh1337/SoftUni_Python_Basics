days = int(input())
hours_per_day = int(input())
total_fee = 0
daily_fee = 0

for i in range (1, days + 1):
    daily_fee = 0
    for k in range (1, hours_per_day + 1):
        if i % 2 == 0 and k % 2 != 0:
            parking_fee = 2.50
        elif i % 2 != 0 and k % 2 == 0:
            parking_fee = 1.25
        else:
            parking_fee = 1

        daily_fee += parking_fee

    total_fee += daily_fee
    print(f'Day: {i} - {daily_fee:.2f} leva')

print(f'Total: {total_fee:.2f} leva')