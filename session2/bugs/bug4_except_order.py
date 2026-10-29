# Find the bug 4: the first matching except wins
# Fix: specific exceptions first, general ones last

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division durch 0")
except Exception:
    print("Irgendein Fehler")
