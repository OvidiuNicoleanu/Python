from argparse import ArgumentError
import os

def getAFilesFromFolder(folder, file):
    try:
        if type(folder) != str or type(file) != str:
            raise ArgumentError(None, "Please input strings as arguments!")
        if os.path.exists(folder) == False \
            or os.path.exists(os.path.split(file)[0]) == False:
            raise FileExistsError("Please input existing files!")

        with open(file, mode="w") as fileObject:
            for content in os.listdir(folder):
                if os.path.isfile(folder + "\\" + content) \
                    and content[0] == "A":
                    fileObject.write(folder + "\\" + content + "\n")
    except Exception as e:
        print(e)

inputFolder = input()
outputFile = input()
getAFilesFromFolder(inputFolder, outputFile)