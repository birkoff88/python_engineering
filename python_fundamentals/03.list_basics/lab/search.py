number_of_lines = int(input())
special_word = input()
all_words_list = []
filtered_list = []

for _ in range(number_of_lines):
    sentence = input()
    all_words_list.append(sentence)
    if special_word in sentence:
        filtered_list.append(sentence)

print(all_words_list)
print(filtered_list)
