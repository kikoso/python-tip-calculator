# Extension 3: own Stack class and own exception BracketError with position
PAIRS = {")": "(", "]": "[", "}": "{"}


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


class BracketError(Exception):
    def __init__(self, position, message):
        super().__init__(message)
        self.position = position


def check(text):
    stack = Stack()
    for i, ch in enumerate(text):
        if ch in "([{":
            stack.push((ch, i))
        elif ch in PAIRS:
            if stack.is_empty():
                raise BracketError(i, f"'{ch}' ohne Gegenstück")
            top, pos = stack.pop()
            if top != PAIRS[ch]:
                raise BracketError(i, f"'{ch}' passt nicht zu '{top}'")
    if not stack.is_empty():
        top, pos = stack.pop()
        raise BracketError(pos, f"'{top}' nie geschlossen")


try:
    check("(]")
except BracketError as e:
    print(f"Position {e.position}: {e}")
