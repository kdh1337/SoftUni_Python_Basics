hours = int(input())
minutes = int(input())

added_minutes = minutes + 15

if added_minutes >= 60:
    hours = hours + 1
    minutes = added_minutes - 60
elif added_minutes < 60:
    minutes = added_minutes
if hours > 23:
    hours = 0

end_time = f'{hours}:' + f'0{minutes}'

if minutes < 10:
    print (f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')