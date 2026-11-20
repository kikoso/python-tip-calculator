# Find the bug 3: pop() is LIFO. A queue needs FIFO: deque.popleft()
from collections import deque

queue = deque()
queue.append("Anna")
queue.append("Ben")
queue.append("Cem")
print("Bedient:", queue.popleft())
