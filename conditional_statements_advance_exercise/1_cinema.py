project_type = input()
rows = int(input())
columns = int(input())

total_seatings = rows * columns

total_income = 0.0

if project_type == 'Premiere':
    total_income = total_seatings * 12.00
elif project_type == 'Normal':
    total_income = total_seatings * 7.50
elif project_type == 'Discount':
    total_income = total_seatings * 5.00

print(f'{total_income:.2f} leva')