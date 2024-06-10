import math

tourney_number = int(input())
points = int(input())
final_points = points
W_NUMBER = 0
F_NUMBER = 0
SF_NUMBER = 0

for i in range(1, tourney_number + 1):
    result = input()
    if result == 'W':
        W_NUMBER += 1
        final_points += 2000
    elif result == 'F':
        F_NUMBER += 1
        final_points += 1200
    elif result == 'SF':
        SF_NUMBER += 1
        final_points += 720

avg_points = (final_points - points) / tourney_number
win_rate = W_NUMBER / tourney_number * 100

print(f'Final points: {final_points}')
print(f'Average points: {math.floor(avg_points)}')
print(f'{win_rate:.2f}%')