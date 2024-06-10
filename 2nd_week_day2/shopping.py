budget = float(input())
GPU_number = int(input())
CPU_number = int(input())
RAM_number = int(input())

GPU_price = 250
GPU_cost = GPU_price * GPU_number

CPU_price = 0.35 * GPU_cost
CPU_cost = CPU_price * CPU_number

RAM_price = 0.1 * GPU_cost
RAM_cost = RAM_price * RAM_number

total_cost = GPU_cost + CPU_cost + RAM_cost

if GPU_number > CPU_number:
    total_cost = total_cost - (total_cost * 0.15)

money_left = budget - total_cost
money_needed = total_cost - budget

if money_left >= 0:
    print(f"You have {money_left:.2f} leva left!")
elif money_left < 0:
    print(f"Not enough money! You need {abs(money_needed):.2f} leva more!")