# Exercise: reverse a string with a stack


def reverse_string(text):
    stack = []
    for ch in text:
        stack.append(ch)
    result = ""
    while stack:
        result += stack.pop()
    return result


print(reverse_string("Stack"))
print(repr(reverse_string("")))
