# Find the bug 6: without () total is the function itself, not its result


def total():
    return 4.5 + 3.0


print(f"Summe: {total()}")
