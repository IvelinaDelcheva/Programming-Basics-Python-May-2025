flower_type = input()
number_of_flowers = int(input())
budget = int(input())

total_price = 0.0

if flower_type == 'Roses':
    total_price = number_of_flowers * 5
    if number_of_flowers > 80:
        total_price -= total_price * 0.10
elif flower_type == 'Dahlias':
    total_price = number_of_flowers * 3.80
    if number_of_flowers > 90:
        total_price -= total_price * 0.15
elif flower_type == 'Tulips':
    total_price = number_of_flowers * 2.80 
    if number_of_flowers > 80:
        total_price -= total_price * 0.15
elif flower_type == 'Narcissus':
    total_price = number_of_flowers * 3 
    if number_of_flowers < 120:
        total_price += total_price * 0.15
elif flower_type == 'Gladiolus':
    total_price = number_of_flowers * 2.50 
    if number_of_flowers < 80:
        total_price += total_price * 0.20

if total_price <= budget:
    print(f'Hey, you have a great garden with {number_of_flowers} {flower_type} and {(budget - total_price):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total_price - budget):.2f} leva more.')