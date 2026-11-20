# Bonus 1: stack with get_min in O(1) using a second stack of minimums


class MinStack:
    def __init__(self):
        self._items = []
        self._mins = []

    def push(self, x):
        self._items.append(x)
        if not self._mins or x < self._mins[-1]:
            self._mins.append(x)
        else:
            self._mins.append(self._mins[-1])

    def pop(self):
        self._mins.pop()
        return self._items.pop()

    def get_min(self):
        return self._mins[-1]


s = MinStack()
for x in [5, 3, 7, 2]:
    s.push(x)
print(s.get_min())
s.pop()
print(s.get_min())
