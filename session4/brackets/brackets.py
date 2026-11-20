# Practice session 4: bracket checker with a stack
PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(text):
    stack = []
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in PAIRS:
            if not stack or stack.pop() != PAIRS[ch]:
                return False
    return len(stack) == 0


def main():
    print("Klammer-Prüfer (leere Zeile beendet)")
    while True:
        line = input("> ")
        if line == "":
            break
        if is_balanced(line):
            print("OK")
        else:
            print("Fehler: Klammern passen nicht")


if __name__ == "__main__":
    main()
