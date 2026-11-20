# Bonus 4: palindrome check with a deque, comparing both ends
from collections import deque


def is_palindrome(text):
    d = deque(text.lower())
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


print(is_palindrome("Reliefpfeiler"))
print(is_palindrome("Python"))
