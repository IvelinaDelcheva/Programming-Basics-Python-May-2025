price_of_the_trip = float(input())
total_puzzles = int(input())
total_dolls = int(input())
total_bears = int(input())
total_minions = int(input())
total_trucks = int(input())

price_pizzles = 2.60
price_dolls = 3.00
price_bears = 4.10
price_minions = 8.20
price_trucks = 2.00

#  \ this is to move to a new line withouth breaking the code 
total_price = (total_puzzles * price_pizzles) + (total_dolls * price_dolls)+ \
    (total_bears * price_bears) + (total_minions * price_minions) + (total_trucks * price_trucks)
total_quantity_toys = total_puzzles + total_dolls + total_bears + total_minions + total_trucks

if total_quantity_toys >= 50:
    discount = total_price * 0.25
    total_price -= discount
    
rent = total_price * 0.1

if (total_price - rent) >= price_of_the_trip:
    money_left = total_price - rent - price_of_the_trip
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = total_price - rent - price_of_the_trip
    print(f'Not enough money! {abs(money_needed):.2f} lv needed.')

