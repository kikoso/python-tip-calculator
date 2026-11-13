# Duplicates in O(n) with a set (instead of O(n^2) with two loops)


def has_duplicates(items):
    seen = set()
    for x in items:
        if x in seen:
            return True
        seen.add(x)
    return False


print(has_duplicates([3, 1, 4, 1]))
print(has_duplicates([3, 1, 4]))
