deposit_amount = float(input())
deposit_period = int(input())
yearly_interest = float(input())

calculate_interest = deposit_amount * (yearly_interest / 100 )
interest_per_month = calculate_interest / 12

result = deposit_amount + (deposit_period * interest_per_month)

print(result)