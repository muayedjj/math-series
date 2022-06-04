"""
The following three sets of test functions will test the functionality of the three functions
0000, 0000, 0000 defined in the 'series.py' file found in the 'math_series' folder of this project.
"""
from math_series import series


# Fibonacci tests
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


# Lucas tests
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


# Sum Function tests
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
