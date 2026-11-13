# Level 1: count how often the recursive version calls itself

from fibonacci import fib_iter

calls = 0


def fib_rec(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


for n in [10, 20, 25]:
    calls = 0
    fib_rec(n)
    print(n, calls, 2 * fib_iter(n + 1) - 1)
