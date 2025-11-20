money_needed_for_holiday = float(input())
available_money = float(input())
cant_save = False
spend_counter = 0
total_days = 0

while True:
    action = input()
    current_money = float(input())
    total_days += 1
    if action == 'spend':
        spend_counter += 1
        available_money -= current_money
        if spend_counter == 5:
            cant_save = True
            break
    elif action == 'save':
        spend_counter = 0
        if available_money < 0:
            available_money = 0
        available_money += current_money
        if available_money >= money_needed_for_holiday:
            break
    

if cant_save:
    print('You can\'t save the money.')
    print(f'{total_days}')
else:
    print(f'You saved the money for {total_days} days.')
