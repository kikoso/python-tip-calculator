# Bonus 2: queue built from two stacks. dequeue is amortised O(1)


class TwoStackQueue:
    def __init__(self):
        self._in = []
        self._out = []

    def enqueue(self, x):
        self._in.append(x)

    def dequeue(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        if not self._out:
            raise IndexError("dequeue aus leerer Queue")
        return self._out.pop()


q = TwoStackQueue()
for x in [1, 2, 3]:
    q.enqueue(x)
print(q.dequeue())
q.enqueue(4)
print(q.dequeue(), q.dequeue(), q.dequeue())
