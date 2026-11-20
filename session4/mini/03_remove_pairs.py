# Bonus 3: remove adjacent duplicates with a stack


def remove_pairs(text):
    stack = []
    for ch in text:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


print(remove_pairs("abbaca"))
print(repr(remove_pairs("aabb")))
