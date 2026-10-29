# Mini exercise 3: average that raises ValueError for an empty list


def average(numbers: list) -> float:
    """Return the mean, raise ValueError if empty."""
    if not numbers:
        raise ValueError("Liste ist leer")
    return sum(numbers) / len(numbers)


print(average([2, 4, 9]))

try:
    print(average([]))
except ValueError as e:
    print(f"Fehler: {e}")
