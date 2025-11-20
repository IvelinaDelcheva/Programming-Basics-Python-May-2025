days_for_stay = int(input())
room_type = input()
score = input()

total_price = 0

if days_for_stay < 10:

    if room_type == 'room for one person':
        total_price = (days_for_stay - 1) * 18

    elif room_type == 'apartment':
        total_price = (days_for_stay - 1) * 25
        total_price -= total_price * 0.3

    elif room_type == 'president apartment':
        total_price = (days_for_stay - 1) * 35
        total_price -= total_price * 0.1

elif 10 <= days_for_stay <= 15:
    
    if room_type == 'room for one person':
        total_price = (days_for_stay - 1) * 18

    elif room_type == 'apartment':
        total_price = (days_for_stay - 1) * 25
        total_price -= total_price * 0.35

    elif room_type == 'president apartment':
        total_price = (days_for_stay - 1) * 35
        total_price -= total_price * 0.15
elif days_for_stay > 15:
        
    if room_type == 'room for one person':
        total_price = (days_for_stay - 1) * 18

    elif room_type == 'apartment':
        total_price = (days_for_stay - 1) * 25
        total_price -= total_price * 0.50

    elif room_type == 'president apartment':
        total_price = (days_for_stay - 1) * 35
        total_price -= total_price * 0.20


if score == 'positive':
    total_price += total_price * 0.25
elif score == 'negative':
    total_price -= total_price * 0.1

print(f'{total_price:.2f}')
