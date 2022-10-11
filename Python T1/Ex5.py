import math

n = int(input("Input n:"))

matrix = []
for i in range(n):
    line = []
    for j in range(n):
        line.append(input("Input matrix {} {}:".format(i, j)))
    matrix.append(line)

lin = 0
col = 0
cond = True
while cond == True:
    for j in range(col, n - col):
        print(matrix[lin][j])
    col = n - col - 1
    lin += 1

    for i in range(lin, n - lin):
        print(matrix[i][col])
    lin = n - lin

    for j in range(col, n - col - 2, -1):
        print(matrix[lin][j])
    col = n - col - 1
    lin -= 1

    for i in range(lin, n - lin - 2, -1):
        print(matrix[i][col])
    lin = n - lin - 1
    col += 1

    if lin == math.floor(n/2):
        cond = False

        if n % 2 != 0:
            print(matrix[lin][col])
        else:
            print(matrix[lin][col])
            print(matrix[lin][col + 1])
            print(matrix[lin + 1][col])
            print(matrix[lin + 1][col + 1])