a = int(input("Input a:"))
b = int(input("Input b:"))


r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
print(b)