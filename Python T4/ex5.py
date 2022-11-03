from argparse import ArgumentError
from operator import indexOf
import os

def searchText(target, to_search):
    try:
        if type(target) != str or type(to_search) != str:
            raise ArgumentError(None, "Please input string arguments!")
        elif os.path.exists(target) == False:
            raise FileExistsError("Please input a valid path!")
    except Exception as e:
        print(e)

    result = list()

    if os.path.isfile(target) == True:
        try:
            with open(target, "r") as fileObject:
                data = fileObject.read()
                if data.find(to_search) != -1:
                    result.append(target)
        except Exception as e:
            print(e)
    else:
        for content in os.listdir(target):
            if os.path.isfile(target + "\\" + content) == True:
                try:
                    with open(target + "\\" + content, "r") as fileObject:
                        data = fileObject.read()
                        if data.find(to_search) != -1:
                            result.append(target + "\\" + content)
                except Exception as e:
                    print(e)
    if len(result) == 0:
        raise ValueError("No files containing the text found!")
    return result

inputPath = input()
inputText = input()
print(searchText(inputPath, inputText))