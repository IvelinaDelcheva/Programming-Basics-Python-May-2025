number_of_dancers = int(input())
points = float(input())
season = input()
place = input()

money_award = 0

if place == 'Bulgaria':
    money_award = number_of_dancers * points
    if season == 'summer':
        money_award *= 0.95 
    elif season == 'winter':
        money_award *= 0.92
elif place == 'Abroad':
    money_award = (number_of_dancers * points) + (number_of_dancers * points) * 0.50
    if season == 'summer':
        money_award *= 0.90 
    elif season == 'winter':
        money_award *= 0.85

sum_for_charity = money_award * 0.75
total_sum_after_charity = money_award - sum_for_charity
money_per_dancer = total_sum_after_charity / number_of_dancers

print(f'Charity - {sum_for_charity:.2f}')
print(f'Money per dancer - {money_per_dancer:.2f}')