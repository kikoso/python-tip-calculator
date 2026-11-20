# deque: fast at both ends
from collections import deque

q = deque()
q.append("A")
q.append("B")
q.appendleft("Z")
print(q)
print(q.popleft())
print(q.pop())
print(len(q))
