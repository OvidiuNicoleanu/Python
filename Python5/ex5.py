def my_function(inputList):
    return list(filter(lambda element: type(element) == int or type(element) == float, inputList))
print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))