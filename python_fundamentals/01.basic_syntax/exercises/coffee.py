number_of_coffees = 0
command = input()
while command != "END":
    if command.islower():
        needed_coffees = 1
    else:
        needed_coffees = 2
    if command.lower() == "coding" or \
        command.lower() == "cat" or \
        command.lower() == "dog" or \
        command.lower() == "movie":
        number_of_coffees += needed_coffees
    command = input()
if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)