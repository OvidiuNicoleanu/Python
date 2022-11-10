def my_function(*args, **keywordArgs):
    sum = 0
    for keyword in keywordArgs.keys():
        try:
            if str(keywordArgs[keyword]).isdecimal() == True:
                if type(keywordArgs[keyword]) == int:
                    sum += int(keywordArgs[keyword])
                elif type(keywordArgs[keyword]) == str:
                    sum += int(keywordArgs[keyword])
            else:
                raise TypeError(keywordArgs[keyword] + " is not a valid number!")
        except TypeError as e:
            print(e)
            continue
    return sum

my_functionAnonymous = lambda *args, **keywordArgs: sum([int(val) for val in keywordArgs.values() if str(val).isdecimal() == True])

print(my_function(1, 2, c="4", d="s", e=2))
print(my_functionAnonymous(1, 2.2, c="4", d="s", e=2))

    