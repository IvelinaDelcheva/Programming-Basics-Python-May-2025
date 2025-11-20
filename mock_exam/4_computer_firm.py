number_pcs = int(input())
total_sales = 0
total_rating = 0

for _ in range(number_pcs):
    sales_nd_ratings = int(input())

    rating = sales_nd_ratings % 10
    sales = sales_nd_ratings // 10

    total_rating += rating

    if rating == 2:
        total_sales += 0
    elif rating == 3:
        total_sales += sales * 0.50
    elif rating == 4:
        total_sales += sales * 0.70
    elif rating == 5:
        total_sales += sales * 0.85
    elif rating == 6:
        total_sales += sales

average_rating = total_rating / number_pcs

print(f'{total_sales:.2f}')
print(f'{average_rating:.2f}')
    

