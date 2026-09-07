deposit_amount = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input())

# amount = deposit_amount + term_of_deposit * ((deposit_amount * annual_interest_rate) / 12)
interest = annual_interest_rate / 100
deposit = deposit_amount * interest
interest_per_month = deposit / 12

amount = deposit_amount + (term_of_deposit * interest_per_month)



print(amount)