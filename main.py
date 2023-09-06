import pytest

from main import factorial


def test_factorial_0():

  assert factorial(0) == 1


def test_factorial_5():

  assert factorial(5) == 120


def factorial(n):

  if n == 0:

    return 1

  else:

    return n * factorial(n - 1)
