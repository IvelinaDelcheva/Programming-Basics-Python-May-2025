import sys

n = int(input())
max_number = -sys.maxsize
sum = 0

for _ in range(n):
    input_number = int(input())

    if input_number > max_number:
        max_number = input_number
    
    sum += input_number



if max_number == sum - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    sum = sum - max_number
    print('No')
    print(f'Diff = {abs(sum - max_number)}')
