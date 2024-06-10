exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

difference = arrival_time - exam_time
hours = abs(difference) // 60
minutes = abs(difference) % 60

if arrival_time > exam_time:
    print('Late')
    if 60 > difference > 0:
        print(f'{difference} minutes after the start')
    elif difference >= 60:
        if minutes < 10:
            print(f'{hours}:0{minutes} hours after the start')
        else:
            print(f'{hours}:{minutes} hours after the start')


elif difference <= 0 and difference >= -30:
    print('On time')
    if difference != 0:
        print(f'{abs(difference)} minutes before the start')

elif difference > 30 or difference < -30:
    print('Early')
    if difference > -60:
        print(f'{abs(difference)} minutes before the start')
    else:
        if minutes < 10:
            print(f'{abs(hours)}:0{minutes} hours before the start')
        else:
            print(f'{abs(hours)}:{minutes} hours before the start')