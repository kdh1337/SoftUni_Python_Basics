daily_goal = 10000
steps = input()
total_steps = 0
steps_home = 0

while steps != 'Going home':
    steps = int(steps)
    total_steps += steps
    if total_steps >= daily_goal:
        print('Goal reached! Good job!')
        print(f'{total_steps - daily_goal} steps over the goal!')
        break
    steps = input()

if steps == 'Going home':
    steps_home = int(input())
    total_steps += steps_home
    if total_steps >= daily_goal:
        print('Goal reached! Good job!')
        print(f'{total_steps - daily_goal} steps over the goal!')
    else:
        print(f'{daily_goal - total_steps} more steps to reach goal.')