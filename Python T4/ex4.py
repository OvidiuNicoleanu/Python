from argparse import ArgumentError
import os
import sys

def getUniqueExtensions(inputPath):
    try:
        if type(inputPath) != str:
            raise ArgumentError(None, "Please give a string as input!")
        elif os.path.isdir(inputPath) == False:
            raise FileExistsError(None, "Please give a folder as input!")
    except Exception as e:
        print(e)

    uniqueExtensions = set()
    for content in os.listdir(inputPath):
        if os.path.isfile(inputPath + "\\" + content) == True:
            uniqueExtensions.add(os.path.splitext(content)[1][1:])
    
    return list(uniqueExtensions)

print(getUniqueExtensions(sys.argv[1]))