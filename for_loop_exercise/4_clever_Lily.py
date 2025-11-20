ages = int(input())
washing_machine_price = float(input())
toy_price = int(input())

coeficient = 1
savings = 0

for age in range(1, ages + 1):
    if age % 2 != 0:
        savings += toy_price
    elif age % 2 == 0:
        savings += (coeficient * 10)
        savings -= 1
        coeficient += 1

if savings >= washing_machine_price:
    print(f'Yes! {(savings - washing_machine_price):.2f}')
else:
    print(f'No! {(washing_machine_price - savings):.2f}')

