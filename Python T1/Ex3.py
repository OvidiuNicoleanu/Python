inputString1 = input("Input string 1:")
inputString2 = input("Input string 2:")

counter = 0
index = 0
cond = inputString2[index:].find(inputString1)
while cond != -1:
    counter += 1
    index += cond + 1
    cond = inputString2[index:].find(inputString1)
print(counter)