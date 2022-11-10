import math
import sys

primeNumbers = []
oldlimit = 0

def eratostene(x):
    #gap between prime numbers is around digits*2.3; gross aproximation
    limit = x + len(str(x))*3
    global oldlimit
    global primeNumbers
    if limit > oldlimit:
        oldlimit = limit
    else:
        return

    print("Eratostenes will be generated again.")

    primeNumbers = [i for i in range(2, limit + 1)]

    for i in range(4, limit + 1, 2):
        primeNumbers.remove(i)

    aux = 3
    while aux * aux <= limit:
        if aux in primeNumbers:
            for i in range(aux * aux, limit + 1, aux):
                if i in primeNumbers:
                    primeNumbers.remove(i)
        aux += 2

def getLeastGreaterPrime(x):
    left = 0
    right = len(primeNumbers) - 1
    while left <= right:
        mid = int((left + right) / 2);

        if mid == 0 or mid == len(primeNumbers) - 1:
            return primeNumbers[mid];
        elif primeNumbers[mid] == x:
            return primeNumbers[mid + 1];
        if primeNumbers[mid] < x and primeNumbers[mid + 1] > x:
            return primeNumbers[mid + 1];
        if x < primeNumbers[mid]:
            right = mid - 1
        else:
            left = mid + 1
 
def process_item(x):
    eratostene(x)
    return getLeastGreaterPrime(x)

def main():
    try:
        inputNumber = int(input("Please input a number:"))
    except Exception:
        raise TypeError("Please input a number!")

    print(process_item(inputNumber))

if __name__ == '__main__':
    main()