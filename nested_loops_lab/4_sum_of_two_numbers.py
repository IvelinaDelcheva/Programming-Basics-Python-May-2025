start_interval = int(input())
stop_interval = int(input())
magic_number = int(input())

combinations_counter = 0
result = 0
is_found = False

for x in range(start_interval, stop_interval + 1):
    for y in range(start_interval, stop_interval + 1):
        combinations_counter += 1
        result = x + y
        if result == magic_number:
            is_found = True
            print(f'Combination N:{combinations_counter} ({x} + {y} = {magic_number})')
            break
    if is_found:
        break

if not is_found:
    print(f'{combinations_counter} combinations - neither equals {magic_number}')
