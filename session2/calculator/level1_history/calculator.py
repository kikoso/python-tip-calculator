# Level 1: same module as the main solution
# Robust calculator: the module with all calculations
# Only return and raise here, no print.


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


def calculate(a, op, b):
    if op == "+":
        return add(a, b)
    if op == "-":
        return subtract(a, b)
    if op == "*":
        return multiply(a, b)
    if op == "/":
        return divide(a, b)
    raise ValueError(f"Unbekanntes Zeichen: {op}")
