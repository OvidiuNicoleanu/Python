def my_function(inputList):
    oddNumbers = list(filter(lambda number: number % 2 == 1, inputList))
    evenNumbers = list(filter(lambda number: number not in oddNumbers, inputList))

    result = list(zip(evenNumbers, oddNumbers))

    return result

print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))