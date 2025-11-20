from math import pi

figure = input()

area = 0

if figure == 'square':
    side = float(input())
    area = side * side
elif figure == 'rectangle':
    width = float(input())
    height = float(input())
    area = width * height
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    area = side * height / 2
elif figure == 'circle':
    radius = float(input())
    # ** is to raising to power 
    area = pi * radius ** 2

print(f'{area:.3f}')