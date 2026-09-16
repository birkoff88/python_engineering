PRICE_PENS = 5.80
PRICE_MARKERS = 7.20
PRICE_CLEANER_PER_LITER = 1.20

pens = int(input())
markers = int(input())
cleaner_liters = int(input())
discount_percent = int(input())

total = pens * PRICE_PENS + markers * PRICE_MARKERS + cleaner_liters * PRICE_CLEANER_PER_LITER
total *= 1 - discount_percent / 100

print(total)