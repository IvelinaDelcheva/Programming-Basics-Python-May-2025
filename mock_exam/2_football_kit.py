price_t_shirt = float(input())
total_sum_to_win = float(input())

shorts_price = price_t_shirt * 0.75
socks_price = shorts_price * 0.20
football_shoes = (price_t_shirt + shorts_price) * 2

total_sum = price_t_shirt + shorts_price + socks_price + football_shoes
total_discounted_price = total_sum * 0.85

diff = total_sum_to_win - total_discounted_price

if total_discounted_price >= total_sum_to_win:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_discounted_price:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {diff:.2f} lv. more.')