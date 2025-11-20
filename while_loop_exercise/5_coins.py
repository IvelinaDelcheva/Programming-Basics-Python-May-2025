change = float(input())

coins_counter = 0

while True:

    if change <= 0:
        break

    if change >= 2.00:
        coins_counter += 1
        change -= 2.00

    elif change >= 1.00:
        coins_counter += 1
        change -= 1.00

    elif change >= 0.50:
        coins_counter += 1
        change -= 0.50

    elif  change >= 0.20:
        coins_counter += 1
        change -= 0.20

    elif change >= 0.10:
        coins_counter += 1
        change -= 0.10

    elif change >= 0.05:
        coins_counter += 1
        change -= 0.05

    elif change >= 0.02:
        coins_counter += 1
        change -= 0.02
    else:
        coins_counter += 1
        change = 0
    
    change = round(change, 2)

print(coins_counter)