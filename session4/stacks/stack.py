# Stack class on top of a list, tested with assert


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop aus leerem Stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek auf leerem Stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0


if __name__ == "__main__":
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    print("Alle Tests bestanden")
