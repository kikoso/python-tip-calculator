# Level 1: collect all calculations and print them when quitting

import calculator

history = []

while True:
    line = input("> ")
    if line == "q":
        for entry in history:
            print(entry)
        print("Tschüss")
        break
    try:
        a_text, op, b_text = line.split()
        a = calculator.parse_number(a_text)
        b = calculator.parse_number(b_text)
        result = calculator.calculate(a, op, b)
        history.append(f"{line} = {result}")
        print(result)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Fehler: {e}")
