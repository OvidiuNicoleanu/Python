from argparse import ArgumentError
from audioop import reverse
from operator import indexOf
import os

def analyzeFolder(my_path):
    try:
        if type(my_path) != str:
            raise ArgumentError(None, "Please input a string!")
        if os.path.exists(my_path) == False:
            raise FileExistsError("Please input an existing folder!")
    except Exception as e:
        print(e)

    if os.path.isfile(my_path) == True:
        try:
            with open(my_path, "r") as fileObject:
                return fileObject.read()[-20:]
        except Exception as e:
            print(e)
    else:
        extensionsCount = dict()
        countExtensions(my_path, extensionsCount)
    return sorted(extensionsCount.items(), key = lambda item: item[1], reverse = True)

def countExtensions(folder, extensionsCount):
    for (root, directories, files) in os.walk(folder):
        for file in files:
            key = os.path.splitext(file)[1][1:]

            if key in extensionsCount:
                extensionsCount[key] += 1
            else:
                extensionsCount[key] = 1

        for directory in directories:
            countExtensions(root + "\\" + directory, extensionsCount)

inputPath = input()
print(analyzeFolder(inputPath))
