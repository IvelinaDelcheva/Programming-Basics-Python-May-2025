hour = int(input())
min = int(input())

hours_in_minutes = hour * 60
minutes = hours_in_minutes + min + 15

total_hours = minutes // 60
total_minutes = minutes % 60

if total_hours > 23:
    total_hours = 0

if total_minutes < 10:
    print(f'{total_hours}:0{total_minutes}')
else:
    print(f'{total_hours}:{total_minutes}')