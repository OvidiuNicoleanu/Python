def print_arguments(function):
    def result(*args,**kwargs):
        print("Arguments are {}, {} and will return {}.".format(args, kwargs, function(*args, **kwargs)))
    return result

def multiply_by_two(x):

    return x * 2



def add_numbers(a, b):

    return a + b



augmented_multiply_by_two = print_arguments(multiply_by_two)

x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.



augmented_add_numbers = print_arguments(add_numbers)

x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.