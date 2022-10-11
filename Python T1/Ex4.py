inputString = list(input("Input string:"))
inputString[0] = inputString[0].lower()

counter = 0
for index, character in enumerate(inputString):
    if character.isupper() == True:
        inputString = list(''.join(inputString[:index + counter]) 
        + "_" + character.lower() 
        + ''.join(inputString[index + counter + 1:]))
        counter += 1

print(''.join(inputString))
