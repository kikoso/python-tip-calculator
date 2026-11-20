# Ring buffer: deque(maxlen=n) keeps only the last n values
from collections import deque

last = deque(maxlen=3)
for x in [1, 2, 3, 4, 5]:
    last.append(x)
print(last)
