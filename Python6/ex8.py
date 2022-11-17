import os
import re

def parseDir(directory, regex):
    for root, dirs, files in os.walk(directory):
        for file in files:
            cond1 = False
            cond2 = False

            if re.search(regex, file):
                cond1 = True

            try:
                with open(root + "\\" + file, "r") as fileObj:
                    if re.search(regex, fileObj):
                        cond2 = True
            except Exception as e:
                raise Exception("File issue! " + e)
            
            if cond1 == True and cond2 == True:
                print("<<" + file)
            elif cond1 == True or cond2 == True:
                print(file)