def process(**keywordArgs):
    fibonacci = [0, 1]
    a = 0
    b = 1
    for index in range(2, 1000):
        c = a + b
        a = b
        b = c
        fibonacci.append(c)

    if "filters" in keywordArgs.keys():
        fibonacci = [element for element in fibonacci if all([predicate(element) for predicate in keywordArgs["filters"]])]
    if "offset" in keywordArgs.keys():
        fibonacci = fibonacci[keywordArgs["offset"]:]
    if "limit" in keywordArgs.keys():
        fibonacci = fibonacci[:keywordArgs["limit"]]
    
    return fibonacci

def sum_digits(x):
    return sum(map(int, str(x)))

print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],\
    limit=2,\
    offset=2\
))