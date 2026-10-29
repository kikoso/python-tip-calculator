# Level 2: ** and %, with a dictionary of functions instead of an if chain


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division durch 0")
    return a / b


def parse_number(text):
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"Keine Zahl: {text}")


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": lambda a, b: a ** b,
    "%": lambda a, b: a % b,
}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"Unbekanntes Zeichen: {op}")
    return OPERATIONS[op](a, b)
