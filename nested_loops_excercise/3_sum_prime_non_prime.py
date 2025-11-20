sum_prime_numbers = 0
sum_non_prime_numbers = 0

while True:
    non_prime_number = False
    command = input()
    if command == 'stop':
        break

    number = int(command)
    if number < 0:
        print('Number is negative.')
        continue
    else:
        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                sum_non_prime_numbers += number
                non_prime_number = True
                break
    
    if not non_prime_number:
        sum_prime_numbers += number

print(f'Sum of all prime numbers is: {sum_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_non_prime_numbers}')