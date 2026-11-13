# Level 3: fib_iter(10000) works, fib_memo(10000) hits the recursion limit

from fibonacci import fib_iter, fib_memo

print(len(str(fib_iter(10000))))

fib_memo.cache_clear()
try:
    fib_memo(10000)
except RecursionError as e:
    print(f"RecursionError: {e}")
