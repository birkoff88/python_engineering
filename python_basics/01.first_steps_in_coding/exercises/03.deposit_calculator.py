deposit_sum = float(input())
deposit_period = int (input())
annual_interest = float(input())

total_annual_interest = deposit_sum * (annual_interest / 100)
interest_per_mont = total_annual_interest / 12
total_sum = deposit_sum + (deposit_period * interest_per_mont)

print(total_sum)