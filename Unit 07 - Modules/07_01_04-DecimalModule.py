"""
Let's say you are writing software that handles monetary transactions. If you used Python's built-in floating-point
 arithmetic to calculate a sum, it would result in a weirdly formatted number.

Usually, modules will provide functions or data types that we can then use to solve a general problem, allowing us
 more time to focus on the software that we are building to solve a more specific problem.
"""

from decimal import Decimal

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)


def test_function_please_ignore():
    return True
