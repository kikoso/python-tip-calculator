# Climbing stairs with steps of 1 or 2: in how many ways?
# ways(n) is Fibonacci shifted by one. @cache makes ways(80) instant.

from functools import cache


@cache
def ways(n):
    if n <= 1:
        return 1
    return ways(n - 1) + ways(n - 2)


print(ways(3))
print(ways(10))
print(ways(80))
