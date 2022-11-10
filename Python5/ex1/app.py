import sys
import utils

def main():
    while True:
        userInput = input()
        try:
            inputNumber = int(userInput)
            print("The least greater than {} prime number is {}.".format(inputNumber, utils.process_item(inputNumber)))
        except Exception as e:
            if userInput == "q":
                sys.exit()
            else:
                print(e)

if __name__ == '__main__':
    main()