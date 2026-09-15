PRICE_PACKAGE_PENS = 5.8
PRICE_PACKAGE_MARKERS = 7.20
PRICE_CLEANING_PREPARATION = 1.20

number_package_pens = int(input())
number_package_markers = int(input())
literes_cleaning_preparation = int(input())

percent_discount = int(input())

sum_pens = number_package_pens * PRICE_PACKAGE_PENS
sum_markers = number_package_markers * PRICE_PACKAGE_MARKERS
sum_cleaning = literes_cleaning_preparation * PRICE_CLEANING_PREPARATION

total_sum = sum_pens + sum_markers + sum_cleaning

sum_discount = percent_discount / 100

total_discount = total_sum * sum_discount
total_sum = total_sum - total_discount
print(total_sum)