import math

days_training = int(input())
km_ran = float(input())
km_ran_total = km_ran

goal = 1000

for i in range(1, days_training + 1):
    percent = int(input())
    real_percent = percent / 100
    km_ran += km_ran * real_percent
    km_ran_total += km_ran

if km_ran_total >= 1000:
    print(f"You've done a great job running {math.ceil(km_ran_total - goal)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(goal - km_ran_total)} more kilometers")