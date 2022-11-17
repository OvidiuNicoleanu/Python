import re

def getSubstringsByLength(regexExp, inputText, x):
    return [substring for substring in re.findall(regexExp, inputText) if len(substring) == x]

print(getSubstringsByLength("(\d+)","Color from pixel 20,30 is 123",2))