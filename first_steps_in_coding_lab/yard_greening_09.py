square_meters = float(input())

total_sum_wtohout_discount = square_meters * 7.61
discount = total_sum_wtohout_discount * 0.18

total_sum_with_discount = total_sum_wtohout_discount - discount

print(f'The final price is: {total_sum_with_discount} lv."')
print(f'The discount is: {discount} lv."')

