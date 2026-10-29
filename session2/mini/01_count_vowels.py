# Mini exercise 1: count vowels, umlauts included


def count_vowels(text: str) -> int:
    """Count vowels, including umlauts."""
    count = 0
    for char in text.lower():
        if char in "aeiouäöü":
            count += 1
    return count


print(count_vowels("Informatik"))
print(count_vowels("Öl"))
