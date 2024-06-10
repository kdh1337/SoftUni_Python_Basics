time = int(input())
day = input()

if time >= 10 and time <= 18 and (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday'
                                  or day == 'Friday' or day == 'Saturday'):
    print('open')
else:
    print('closed')