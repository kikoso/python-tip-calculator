# Extension 1: report the position of the error and mark it with ^
PAIRS = {")": "(", "]": "[", "}": "{"}


def find_error(text):
    stack = []
    for i, ch in enumerate(text):
        if ch in "([{":
            stack.append((ch, i))
        elif ch in PAIRS:
            if not stack:
                return i, f"'{ch}' ohne Gegenstück"
            top, pos = stack.pop()
            if top != PAIRS[ch]:
                return i, f"'{ch}' passt nicht zu '{top}'"
    if stack:
        top, pos = stack[-1]
        return pos, f"'{top}' nie geschlossen"
    return None


if __name__ == "__main__":
    text = "x = (a[1)]"
    pos, msg = find_error(text)
    print(text)
    print(" " * pos + "^", msg)
