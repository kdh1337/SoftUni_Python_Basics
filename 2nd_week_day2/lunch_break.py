import math

series_name = input()
episode_length = float(input())
break_length = float(input())

lunch_time = 0.125 * break_length
chill_time = 0.25 * break_length

time_left = break_length - lunch_time - chill_time
time_needed = math.ceil(time_left - episode_length)
time_for_episode = math.ceil(episode_length - time_left)

if time_left >= episode_length:
    print(f"You have enough time to watch {series_name} and left with {time_needed} minutes free time.")
elif time_left < episode_length:
    print(f"You don't have enough time to watch {series_name}, you need {abs(time_for_episode)} more minutes.")