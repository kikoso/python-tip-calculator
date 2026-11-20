# append (amortised O(1)) against insert(0, x) (O(n)), measured
import time

n = 100_000
start = time.perf_counter()
a = []
for i in range(n):
    a.append(i)
print("append:", round(time.perf_counter() - start, 4))

start = time.perf_counter()
b = []
for i in range(n):
    b.insert(0, i)
print("insert:", round(time.perf_counter() - start, 4))
