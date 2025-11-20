n = int(input())

start_number = '1111'
stop_number = '9999'

start_1, start_2, start_3, start_4 = start_number[0], start_number[1], start_number[2], start_number[3]
stop_1, stop_2, stop_3, stop_4 = stop_number[0], stop_number[1], stop_number[2], stop_number[3]

for number_1 in range(int(start_1), int(stop_1) + 1):
    for number_2 in range(int(start_2), int(stop_2) + 1):
        for number_3 in range(int(start_3), int(stop_3) + 1):
            for number_4 in range(int(start_4), int(stop_4) + 1):
                if n % number_1 == 0 and n % number_2 == 0 \
                and n % number_3 == 0 and n % number_4 == 0:
                    print(f'{number_1}{number_2}{number_3}{number_4}', end = ' ')
