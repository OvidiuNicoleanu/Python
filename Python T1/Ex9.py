inputString = list(input("Input string:"))

max = 0
for ascii in range(97, 123):
    character = chr(ascii)
    if inputString.count(character) > max:
        max = inputString.count(character)
        letter = character
    if inputString.count(character.upper()) > max:
        max = inputString.count(character)
        letter = character.upper()

print(letter)