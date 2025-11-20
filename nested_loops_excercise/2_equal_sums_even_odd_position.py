number_1 = int(input())
number_2 = int(input())



for number in range(number_1, number_2 + 1):
    sum_even_positions = 0
    sum_odd_positions = 0
    for idx, digit in enumerate(str(number)):

        if idx % 2 == 0:
            sum_even_positions += int(digit)
        elif idx % 2 != 0:
            sum_odd_positions += int(digit)
        
    if sum_even_positions == sum_odd_positions:
        print(number, end = ' ')