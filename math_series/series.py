# Fibonacci
def fibonacci(num):
    if num < 0 or type(num) != int:
        return "Only Natural Numbers are allowed"
    elif num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def lucas(num):
    if num < 0 or type(num) != int:
        return "Only Natural Numbers are allowed"
    elif num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def sum_series(num: int, a=0, b=1):
    if num == 0:
        return a
    elif num == 1:
        return b
    elif num > 1 and type(num) == int:
        return sum_series(num - 1, a, b) + sum_series(num - 2, a, b)
    else:
        return "Only Natural Numbers Are Allowed"
