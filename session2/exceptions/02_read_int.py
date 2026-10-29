# Exceptions 2: ask until the input is a whole number in the range


def read_int(prompt, low, high):
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("Bitte eine ganze Zahl")
            continue
        if low <= value <= high:
            return value
        print(f"Bitte zwischen {low} und {high}")


grade = read_int("Note (1-6): ", 1, 6)
print(f"Gewählt: {grade}")
