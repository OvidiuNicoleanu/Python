import re
def matchStrings(inputString, regularExps):
    return [substring 
        for substring in inputString 
            if any(
                [re.search(regExp, substring) 
                for regExp in regularExps]
            )
    ]

print(matchStrings("Color from pixel 20,30 is 123", ["((\d+),(\d+))[^\d]*(\d+)"]))