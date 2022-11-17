import re

def splitText(inputText):
    return re.findall("\w+", inputText)

print(splitText("Aurel Vlaicu a fost un aviator R0man 333 4jjr"))