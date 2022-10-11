import enum
import math
textList = list(input("Input text: "))

start = -1
finish = -1

for index, character in enumerate(textList):
    if start == -1:
        if character.isdigit() == True:
            start = index
    elif textList[index - 1].isdigit() == True and character.isdigit() == False:
        finish = index - 1
        break

if start != -1 and finish == -1:
    finish = len(textList) - 1

if start == -1 and finish == -1:
    print("No number.")
else:
    print(''.join(textList[start:finish + 1]))
