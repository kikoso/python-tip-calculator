# Fibonacci race: check that all three agree, then time them

import time
from fibonacci import fib_rec, fib_iter, fib_memo


def measure(func, n):
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start


for n in range(16):
    assert fib_rec(n) == fib_iter(n) == fib_memo(n)

print(" n   rekursiv    iterativ    memo")
for n in [10, 20, 25, 30]:
    fib_memo.cache_clear()
    t_rec = measure(fib_rec, n)
    t_iter = measure(fib_iter, n)
    t_memo = measure(fib_memo, n)
    print(f"{n:>2}   {t_rec:.6f}    {t_iter:.6f}    {t_memo:.6f}")
