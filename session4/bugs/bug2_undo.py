# Find the bug 2: check that the stack is not empty before pop
history = []


def undo():
    if not history:
        print("Nichts rückgängig zu machen")
        return
    action = history.pop()
    print("Rückgängig:", action)


undo()
history.append("Text tippen")
undo()
