money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integers = list(map(int, money_as_string))
beggars_sum = []
for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for index in range(current_beggar, len(money_as_integers), number_of_beggars):
        current_beggar_sum += money_as_integers[index]
    beggars_sum.append(current_beggar_sum)
print(beggars_sum)