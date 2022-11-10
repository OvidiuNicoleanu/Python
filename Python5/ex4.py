import re

def my_function(*args, **keywordArgs):
    result = []
    for arg in args:
        if type(arg) == dict:
            if len(arg.keys()) >= 2:
                # condition = [key for key in arg.keys() if type(key) == str and re.match(pattern, key)]
                condition = [key for key in arg.keys() if type(key) == str  and len(key) >= 3]
                if len(condition) > 0:
                    result.append(arg)
    for arg in keywordArgs:
        if type(keywordArgs[arg]) == dict:
            if len(keywordArgs[arg].keys()) >= 2:
                condition = [key for key in keywordArgs[arg].keys() if type(key) == str and len(key) >= 3]
                if len(condition) > 0:
                    result.append(keywordArgs[arg])
    return result

print(my_function(\
 {1: 2, 3: 4, 5: 6}, \
 {'a': 5, 'b': 7, 'c': 'e'}, \
 {2: 3}, \
 [1, 2, 3],\
 {'abc': 4, 'def': 5},\
 3764,\
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},\
 test={1: 1, 'test': True}
))
     