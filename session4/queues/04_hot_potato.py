# Exercise: hot potato with deque.rotate
from collections import deque


def hot_potato(names, k):
    q = deque(names)
    while len(q) > 1:
        q.rotate(-k)
        print("Raus:", q.popleft())
    return q[0]


names = ["Anna", "Ben", "Cem", "Dana", "Emil"]
print("Sieger:", hot_potato(names, 2))
