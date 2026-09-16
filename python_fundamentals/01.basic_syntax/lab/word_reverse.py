word = input()
final_word = ""

for index in range(len(word) -1, -1, -1):
    final_word += word[index]
print(final_word)