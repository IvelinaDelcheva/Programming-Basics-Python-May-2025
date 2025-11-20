time = int(input())
day_of_week = input()

working_hours = 10 <= time <= 18
working_days = day_of_week == 'Monday' \
    or day_of_week == 'Tuesday' \
    or day_of_week == 'Wednesday' \
    or day_of_week == 'Thursday' \
    or day_of_week == 'Friday' \
    or day_of_week == 'Saturday' \

if working_hours and working_days:
    print('open')
else:
    print('closed')