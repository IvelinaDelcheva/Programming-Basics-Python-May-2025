import sys 

min_number = sys.maxsize

command = input()
while command != 'Stop':
    input_number = int(command)

    if input_number < min_number:
        min_number = input_number

    command = input()

print(min_number)