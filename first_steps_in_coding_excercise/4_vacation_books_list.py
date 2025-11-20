from math import floor

total_pages_in_current_book = int(input())
read_pages_per_hour = int(input())
total_days_per_book = int(input())

hours_needed_per_book = floor(total_pages_in_current_book / read_pages_per_hour)
hours_needed_per_day = floor(hours_needed_per_book/ total_days_per_book)

print(hours_needed_per_day)