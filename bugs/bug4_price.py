# Find the bug 4: the price
# Bug: a str and a float cannot be joined with +, that gives a TypeError.

price = 3.50 * 2

# Fix 1: convert with str()
print("Preis: " + str(price) + " EUR")

# Fix 2, usually better: an f-string with two decimals
print(f"Preis: {price:.2f} EUR")
