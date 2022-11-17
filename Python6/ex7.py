import re

def checkCNP(inputText):
    if re.match(r"[1-8]\d\d(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{6}$", inputText):
        return True
    return False

print(checkCNP("5010110226714"))
print(checkCNP("Aurel Vlaicu"))