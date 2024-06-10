from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

water_slow = floor(distance_in_meters / 15) * 12.5
total_time = (time_in_seconds_per_meter * distance_in_meters) + water_slow
time_difference = record_in_seconds - total_time

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
elif total_time >= record_in_seconds:
    print(f"No, he failed! He was {abs(time_difference):.2f} seconds slower.")