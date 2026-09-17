number = input()
result = ""

for digit in range(9, -1, -1):
    for char in number:
        if char == str(digit):
            result += char

print(result)