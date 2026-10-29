# Find the bug 2: the greeting
# Bug: the f before the quotes was missing, so {name} was printed literally.

name = "Ana"
print(f"Hallo {name}, willkommen!")
