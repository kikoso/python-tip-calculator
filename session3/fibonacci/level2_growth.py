# Level 2: how much slower does each n + 1 get? (about 1.6, the golden ratio)

import time
from fibonacci import fib_rec


def measure(func, n):
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start


previous = measure(fib_rec, 20)
for n in range(21, 29):
    current = measure(fib_rec, n)
    print(f"{n}: Faktor {current / previous:.2f}")
    previous = current
