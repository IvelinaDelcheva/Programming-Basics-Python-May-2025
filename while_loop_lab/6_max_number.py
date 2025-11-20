import sys

max_number = -sys.maxsize

command = input()
while command != 'Stop':
    input_number = int(command)

    if input_number > max_number:
        max_number = input_number

    command = input()

print(max_number)