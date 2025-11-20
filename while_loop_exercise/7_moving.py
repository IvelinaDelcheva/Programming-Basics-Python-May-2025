# 1.	Широчина на свободното пространство - цяло число;
# 2.	Дължина на свободното пространство - цяло число;
# 3.	Височина на свободното пространство - цяло число;
# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
# Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.

height = int(input())
lenght = int(input())
width = int(input())

total_free_space = height * width * lenght
space_taken = 0
no_more_space = False

command = input()
while command != 'Done':
    number_of_boxes = int(command)
    space_taken += number_of_boxes

    if space_taken >= total_free_space:
        no_more_space = True
        break
    command = input()

if no_more_space:
    print(f'No more free space! You need {space_taken - total_free_space} Cubic meters more.')
else:
    print(f'{total_free_space - space_taken} Cubic meters left.')