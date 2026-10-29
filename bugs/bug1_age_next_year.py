# Find the bug 1: age next year
# Bug: input() returns a str, and "20" + 1 is a TypeError.
# Fix: convert the input with int().

age = int(input("Alter: "))
print(f"Nächstes Jahr: {age + 1}")
