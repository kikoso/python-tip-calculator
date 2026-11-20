# Homework session 3 (easy): reverse and count_char, recursive, without loops and without [::-1]


def reverse(text):
    if text == "":
        return ""
    return reverse(text[1:]) + text[0]


def count_char(text, char):
    if text == "":
        return 0
    first = 1 if text[0] == char else 0
    return first + count_char(text[1:], char)


print(reverse("Hallo"))
print(count_char("Banane", "a"))
