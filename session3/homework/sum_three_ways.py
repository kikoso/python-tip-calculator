# Homework session 3 (medium): sum 1..n with a loop O(n), recursion O(n) and a formula O(1)
import time


def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_rec(n):
    return 0 if n == 0 else n + sum_rec(n - 1)


def sum_formula(n):
    return n * (n + 1) // 2


n = 900
print(sum_loop(n), sum_rec(n), sum_formula(n))

for f in (sum_loop, sum_rec, sum_formula):
    start = time.perf_counter()
    f(n)
    print(f.__name__, round(time.perf_counter() - start, 6))
