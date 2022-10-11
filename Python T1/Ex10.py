inputString = input("Input string:")

counter = 0
index = 0
cond = inputString[index:].find(" ")

while cond != - 1:
    if inputString[index - 1] != "_" and inputString[index + 1] != "_":
        counter += 1
    index += cond + 1
    cond = inputString[index:].find(" ")

if counter == 0 and len(inputString != 0):
    counter = 1
elif counter != 0:
    counter += 1

print(counter)
