processor_price_usd = float(input())
video_card_price_usd = float(input())
ram_memory_card_price_usd = float(input())
ram_memory_number = int(input())
discount = float(input())

processor_price_bgn = processor_price_usd * 1.57
video_card_price_bgn = video_card_price_usd * 1.57
ram_memory_card_price_bng = ram_memory_card_price_usd * 1.57
total_ram_memory_price_bgn = ram_memory_card_price_bng * ram_memory_number

processor_discount_price = processor_price_bgn - (processor_price_bgn * discount)
video_card_discount_price = video_card_price_bgn - (video_card_price_bgn * discount)

total_price = processor_discount_price + video_card_discount_price + total_ram_memory_price_bgn

print(f'Money needed - {total_price:.2f} leva.')




