# Exceptions 1: safe division


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Warnung: Division durch 0")
        return None


print(safe_divide(10, 4))
print(safe_divide(1, 0))
