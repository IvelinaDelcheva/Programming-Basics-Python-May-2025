pencils = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())

one_pack_of_pencils_price = 5.80
one_pack_of_markers_price = 7.20
detergent_per_liter = 1.20

total_costs_pencils = pencils * one_pack_of_pencils_price
total_costs_markers = markers * one_pack_of_markers_price
total_costs_detergent = detergent * detergent_per_liter

total_costs = total_costs_pencils + total_costs_markers + total_costs_detergent
total_costs_with_discount = total_costs - (total_costs * (discount / 100))

print(total_costs_with_discount)