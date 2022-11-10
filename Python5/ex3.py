def my_function(inputString):
    if type(inputString) != str:
        raise TypeError("Please input a string!")
    else:
        return list(character for character in inputString if character.lower() in ['a', 'e', 'i', 'o', 'u'])

my_functionAnonymous = lambda inputString: [character for character in inputString if character.lower() in ['a', 'e', 'i', 'o', 'u']]

my_functionFilter = lambda inputString: list(filter(lambda character: character.lower() in "aeiou", inputString))

inputString = "Programming in Python is fun"
print(my_function(inputString))
print(my_functionAnonymous(inputString))
print(my_functionFilter(inputString))