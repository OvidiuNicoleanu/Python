from argparse import ArgumentError
import os

def getExtensions(folderPath):
    try:
        if type(folderPath) != str:
            raise ArgumentError(None, "Please input a string!")
        if os.path.exists(folderPath) == False:
            raise FileExistsError("Please input an existing folder!")
    except Exception as e:
        print(e)
    
    return [os.path.splitext(x)[1][1:] \
        for x in os.listdir(folderPath) \
            if os.path.isfile(folderPath + "\\" + x)]

inputPath = input()
print(getExtensions(inputPath))