# Mini exercise 4: discount with checks (guard clauses)


def apply_discount(price: float, percent: float = 10) -> float:
    """Return the price after a percentage discount."""
    if price < 0:
        raise ValueError("Preis darf nicht negativ sein")
    if not 0 <= percent <= 100:
        raise ValueError("Rabatt muss zwischen 0 und 100 liegen")
    return round(price * (1 - percent / 100), 2)


print(apply_discount(80))
print(apply_discount(80, 25))

try:
    apply_discount(80, 150)
except ValueError as e:
    print(f"Fehler: {e}")
