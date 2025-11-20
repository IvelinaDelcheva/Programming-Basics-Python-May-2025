budget = float(input())
number_of_video_carts = int(input())
number_of_processors = int(input())
number_of_ram_memory = int(input())

video_cart_price = 250.00
total_sum_video_carts = number_of_video_carts * video_cart_price

processor_price = (number_of_video_carts * video_cart_price) * 0.35
total_sum_for_pricessors = number_of_processors * processor_price

ram_memory_price = (number_of_video_carts * video_cart_price) * 0.1
total_sum_for_ram_memory = number_of_ram_memory * ram_memory_price

total_sum = total_sum_video_carts + total_sum_for_pricessors + total_sum_for_ram_memory

if number_of_video_carts > number_of_processors:
    total_sum = total_sum - (total_sum * 0.15)

diff = abs(budget - total_sum)

if total_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')



