n = int(input())
current_num = 1
is_equal = False

for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(current_num, end= ' ')
        
        current_num += 1
        if current_num >= n + 1:
            is_equal = True
            break
    if is_equal:
        break
    print()

        
        