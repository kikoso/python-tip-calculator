# Queue class on top of collections.deque
from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue aus leerer Queue")
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("front auf leerer Queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue("Anna")
    q.enqueue("Ben")
    print(q.dequeue())
    print(q.front())
