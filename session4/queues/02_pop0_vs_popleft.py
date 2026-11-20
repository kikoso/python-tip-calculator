# Exercise: list.pop(0) (O(n)) against deque.popleft() (O(1)), measured
import time
from collections import deque

lst = list(range(100_000))
start = time.perf_counter()
while lst:
    lst.pop(0)
print("pop(0): ", round(time.perf_counter() - start, 4))

d = deque(range(100_000))
start = time.perf_counter()
while d:
    d.popleft()
print("popleft:", round(time.perf_counter() - start, 4))
