# Fibonacci three ways

from functools import cache


def fib_rec(n):
    """Fibonacci, recursive. O(2^n) time."""
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    """Fibonacci, iterative. O(n) time, O(1) space."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@cache
def fib_memo(n):
    """Fibonacci, memoized. O(n) time and space."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)
