number = int(input("Input n:"))

counter = 0
while number != 0:
    if number % 2 != 0:
        counter += 1
    number //= 2

print(counter)