# Find the bug 5: list.pop(0) is O(n). deque.popleft() is O(1)
from collections import deque

jobs = deque(f"Auftrag {i}" for i in range(200_000))
while jobs:
    job = jobs.popleft()
    # drucken ...
print("Fertig")
