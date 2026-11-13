# Find the bug 6: range(n + 1) ran once too often


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib(5))
