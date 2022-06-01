from math_series import series
# Nth integer of the Fibonacci sequence
"""
A function that, given an integer as an argument, returns 
the Fibonacci number that's at the position corresponding to that 
integer in The Fibonacci Sequence, in which each number is 
the sum of the two preceding ones, and the first two numbers
are 0 and 1; corresponding to the positions 0 and 1 respectively
"""


def test_fibo():
    actual = series.fibonacci(10)
    expected = 55
    assert actual == expected


def test_fibo_neg():
    actual = series.fibonacci(-10)
    expected = "Only Natural Numbers are allowed"
    assert actual == expected


def test_fibo_not_int():
    actual = series.fibonacci(10.5)
    expected = "Only Natural Numbers are allowed"
    assert (actual == expected)


# Lucas
"""
A function that, given an integer as an argument, returns 
the lucas number that's at the position corresponding to that 
integer in The Lucas Sequence, in which each number is 
the sum of the two preceding ones, and the first two numbers
are 2 and 1; corresponding to the positions 0 and 1 respectively.
"""


def test_lucas_one():
    actual = series.lucas(1)
    expected = 1
    assert actual == expected


def test_fibo_index_zero():
    actual = series.lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_neg():
    actual = series.lucas(-10)
    expected = "Only Natural Numbers are allowed"
    assert actual == expected


def test_lucas_not_int():
    actual = series.lucas(10.5)
    expected = "Only Natural Numbers are allowed"
    assert (actual == expected)


# Sum Function
"""A function called sum_series with one required parameter and two optional parameters. The required parameter will 
determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will 
determine the first two values for the series to be produced.
Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the 
optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will 
produce other series. Again, you may use recursion or iteration, or both.
"""

def test_sum_zero():
    actual = series.sum_series(0, 2, 3)
    expected = 2
    assert actual == expected


def test_sum_one():
    actual = series.sum_series(1, 2, 3)
    expected = 3
    assert actual == expected


def test_sum_any_nat():
    actual = series.sum_series(5, 1, 2)
    expected = 13
    assert actual == expected


def test_sum_not_nat():
    actual = series.sum_series(-5)
    expected = "Only Natural Numbers Are Allowed"
    assert (actual == expected)
