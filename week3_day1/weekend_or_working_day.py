day = input()

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    day = 'Working day'
elif day == 'Saturday' or day == 'Sunday':
    day = 'Weekend'
else:
    day = 'Error'

print(day)