total_cicken_meals = int(input())
total_fish_meals = int(input())
total_vegeterian_meals = int(input())

price_for_chicken_menu = 10.35
price_for_fish_menu = 12.40
price_for_vegeterian_menu = 8.15
delivery = 2.50

total_price_for_chicken_menu = total_cicken_meals * price_for_chicken_menu
total_price_for_fish_menu = total_fish_meals * price_for_fish_menu
total_price_for_vegeterian_menu = total_vegeterian_meals * price_for_vegeterian_menu

total_price = total_price_for_chicken_menu + total_price_for_fish_menu + total_price_for_vegeterian_menu
dessert_price = total_price * 0.2

final_price = total_price + dessert_price + delivery

print(final_price)
