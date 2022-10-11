inputString = input("Input string:")
vocals = ["a", "e", "i", "o", "u"]

counter = 0
for vocal in vocals:
    counter += inputString.count(vocal)
print(counter)

