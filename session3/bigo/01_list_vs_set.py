# Membership test: list is O(n), set is O(1)

import time

numbers_list = list(range(1_000_000))
numbers_set = set(range(1_000_000))

for name, data in [("Liste", numbers_list), ("Set", numbers_set)]:
    start = time.perf_counter()
    found = 999_999 in data
    duration = time.perf_counter() - start
    print(f"{name}: {duration:.6f} s")
