# Palindrome, recursive: compare the ends, then check the middle


def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


print(is_palindrome("rentner"))
print(is_palindrome("python"))
