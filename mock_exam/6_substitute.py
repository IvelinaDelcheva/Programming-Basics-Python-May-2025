K = int(input())
L = int(input())
M = int(input())
N = int(input())

valid_shifts = 0
enough_shifts = False


for number1 in range(K, 8 + 1):
    for number2 in range(9, L - 1, -1):
        for number3 in range(M, 8 + 1):
            for number4 in range(9 , N - 1, -1):

                if number1 % 2 == 0 and number2 % 2 != 0 and number3 % 2 == 0 and number4 % 2 != 0:
                    if number1 == number3 and number2 == number4:
                        print('Cannot change the same player.')
                    else:
                        valid_shifts += 1
                        print(f'{number1}{number2} - {number3}{number4}')
                    if valid_shifts == 6:
                        enough_shifts = True
                        break
            if enough_shifts:
                break
        if enough_shifts:
            break
    if enough_shifts:
        break
