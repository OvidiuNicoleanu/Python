import math
number = int(input("Input number: "))

digitList = []
for digit in str(number):
    digitList.append(digit)

cond = True
for index in range(len(digitList)):
    if digitList[index] != digitList[len(digitList) - index - 1]:
        cond = False
        break
    if index == math.ceil((len(digitList) / 2)):
        break

if cond == True:
    print("Number is palindrome!")
else:
    print("Number is NOT palindrome!")
