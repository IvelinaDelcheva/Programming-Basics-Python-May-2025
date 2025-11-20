n = int(input())

even_numbers_sum = 0
odd_numbers_sum = 0

for i in range(n):
    number = int(input())

    if i % 2 == 0:
        even_numbers_sum += number
    else:
        odd_numbers_sum += number

diff = abs(even_numbers_sum - odd_numbers_sum)

if even_numbers_sum == odd_numbers_sum:
    print('Yes')
    print(f'Sum = {even_numbers_sum}')
else:
    print('No')
    print(f'Diff = {diff}')
