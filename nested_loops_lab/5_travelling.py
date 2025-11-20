while True:
    destination = input()

    if destination == 'End':
        break
    minimal_budget = float(input())
    saved_money = 0
    
    while True:
        current_savings = float(input())
        saved_money += current_savings
        if saved_money >= minimal_budget:
            print(f'Going to {destination}!')
            break
    
    