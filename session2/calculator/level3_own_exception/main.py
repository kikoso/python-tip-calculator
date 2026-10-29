# Level 3: main.py only catches CalculatorError

import calculator

while True:
    line = input("> ")
    if line == "q":
        print("Tschüss")
        break
    try:
        a, op, b = calculator.parse_line(line)
        print(calculator.calculate(a, op, b))
    except calculator.CalculatorError as e:
        print(f"Fehler: {e}")
