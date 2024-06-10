lenght_centimeters = int(input())
width_centimeters = int(input())
height_centimeters = int(input())
percent = float(input())

volume = lenght_centimeters * width_centimeters * height_centimeters
volume_in_litres = volume / 1000
occupied_volume = percent / 100
volume_water = volume_in_litres * (1 - occupied_volume)

print(volume_water)