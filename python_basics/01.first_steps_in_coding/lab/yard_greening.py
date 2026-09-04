m2 = float(input())

price_per_m2 = 7.61
total_price = m2 * price_per_m2
discount = 0.18 * total_price
total_sum = total_price - discount
print(f"The final price is: {total_sum} lv.")
print(f"The discount is: {discount} lv.")