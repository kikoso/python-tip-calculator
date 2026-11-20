# Extension 2: check a whole file line by line
from level1_position import find_error


def check_file(path):
    with open(path, encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            error = find_error(line)
            if error:
                pos, msg = error
                print(f"Zeile {number}, Spalte {pos + 1}: {msg}")


check_file("beispiel.txt")
