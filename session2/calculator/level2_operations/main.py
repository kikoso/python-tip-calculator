# Level 2: same main.py as the main solution
# Type a calculation like "3 + 4" (with spaces). "q" quits.

import calculator

while True:
    line = input("> ")
    if line == "q":
        print("Tschüss")
        break
    try:
        a_text, op, b_text = line.split()
        a = calculator.parse_number(a_text)
        b = calculator.parse_number(b_text)
        print(calculator.calculate(a, op, b))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Fehler: {e}")
