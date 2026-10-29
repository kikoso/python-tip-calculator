# Level 3: one own exception type for all calculator errors


class CalculatorError(Exception):
    pass


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise CalculatorError("Division durch 0")
    return a / b


def parse_number(text):
    try:
        return float(text)
    except ValueError:
        raise CalculatorError(f"Keine Zahl: {text}") from None


def parse_line(line):
    parts = line.split()
    if len(parts) != 3:
        raise CalculatorError("Format: Zahl Zeichen Zahl")
    return parse_number(parts[0]), parts[1], parse_number(parts[2])


def calculate(a, op, b):
    if op == "+":
        return add(a, b)
    if op == "-":
        return subtract(a, b)
    if op == "*":
        return multiply(a, b)
    if op == "/":
        return divide(a, b)
    raise CalculatorError(f"Unbekanntes Zeichen: {op}")
