"""
Here you will find three functions defined, all of which give the Nth number in a sequence
given the first two numbers and calculating the succeeding sequential pattern following
fibonacci's rule of adding two consecutive numbers to find the third one.
"""


def fibonacci(num):
    """
    Nth integer of the Fibonacci sequence
    A function that, given an integer as an argument, returns
    the Fibonacci number that's at the position corresponding to that
    integer in The Fibonacci Sequence, in which each number is
    the sum of the two preceding ones, and the first two numbers
    are 0 and 1; corresponding to the positions 0 and 1 respectively
    """
    if num < 0 or type(num) != int:
        return "Only Natural Numbers are allowed"
    elif num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def lucas(num):
    """
    A function that, given an integer as an argument, returns
    the lucas number that's at the position corresponding to that
    integer in The Lucas Sequence, in which each number is
    the sum of the two preceding ones, and the first two numbers
    are 2 and 1; corresponding to the positions 0 and 1 respectively.
    """
    if num < 0 or type(num) != int:
        return "Only Natural Numbers are allowed"
    elif num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def sum_series(num: int, a=0, b=1):
    """A function called sum_series with one required parameter and two optional parameters. The required parameter will
    determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and
    will determine the first two values for the series to be produced.
    Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with
    the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters
    will produce other series. Again, you may use recursion or iteration, or both.
    """
    if num == 0:
        return a
    elif num == 1:
        return b
    elif num > 1 and type(num) == int:
        return sum_series(num - 1, a, b) + sum_series(num - 2, a, b)
    else:
        return "Only Natural Numbers Are Allowed"
