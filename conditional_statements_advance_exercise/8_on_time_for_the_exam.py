exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

late_arrival_hour = 0
late_arrival_minutes = 0

exam_total_minutes = (exam_hour * 60) + exam_minutes
arrival_total_minutes = (arrival_hour * 60) + arrival_minutes

exam_arrival_time_difference = abs(exam_total_minutes - arrival_total_minutes)

if arrival_total_minutes > exam_total_minutes:
    print('Late')
    if 1 <= exam_arrival_time_difference <= 59:
        print(f'{exam_arrival_time_difference} minutes after the start')
        
    elif exam_arrival_time_difference > 59:
        late_arrival_hour = exam_arrival_time_difference // 60
        late_arrival_minutes = exam_arrival_time_difference % 60
        if late_arrival_minutes <= 9:
            print(f'{late_arrival_hour}:0{late_arrival_minutes} hours after the start')
        else:
            print(f'{late_arrival_hour}:{late_arrival_minutes} hours after the start')

elif (arrival_total_minutes == exam_total_minutes):
    print('On time')

elif 0 <= exam_arrival_time_difference <= 30:
    print('On time')
    print(f'{exam_arrival_time_difference} minutes before the start')

elif exam_arrival_time_difference < exam_total_minutes:
    print('Early')
    if 1 <= exam_arrival_time_difference <= 59:
        print(f'{exam_arrival_time_difference} minutes before the start')

    elif exam_arrival_time_difference > 59:
        late_arrival_hour = exam_arrival_time_difference // 60
        late_arrival_minutes = exam_arrival_time_difference % 60
        if late_arrival_minutes <= 9:
            print(f'{late_arrival_hour}:0{late_arrival_minutes} hours before the start')
        else:
            print(f'{late_arrival_hour}:{late_arrival_minutes} hours before the start')




