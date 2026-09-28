deposit = float(input())
months = int(input())
annual_percent = float(input())

yearly_interest = deposit * annual_percent / 100
monthly_interest = yearly_interest / 12
total = deposit + months * monthly_interest

print(total)