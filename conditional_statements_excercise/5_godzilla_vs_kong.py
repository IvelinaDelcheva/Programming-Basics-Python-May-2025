movie_budget = float(input())
total_spectators = float(input())
spectators_clothes_price = float(input())

movie_decor = movie_budget * 0.1

if total_spectators > 150:
    discount = spectators_clothes_price * 0.1
    spectators_clothes_price -= discount

total_amount_needed = movie_decor +  (total_spectators * spectators_clothes_price)

if movie_budget >= total_amount_needed:
    money_left = movie_budget - total_amount_needed
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
else:
    money_needed = total_amount_needed - movie_budget
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
