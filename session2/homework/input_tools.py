# Homework session 2 (medium): safe input functions


def read_int(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Bitte eine ganze Zahl")
            continue
        if low <= value <= high:
            return value
        print(f"Bitte zwischen {low} und {high}")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Bitte eine Zahl")


if __name__ == "__main__":
    grade = read_int("Note (1-6): ", 1, 6)
    price = read_float("Preis: ")
    print(grade, price)
