# Find the bug 5: "x not in list" in a loop is O(n^2). A set makes it O(n).


def unique(items):
    result = []
    seen = set()
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


print(len(unique(list(range(100_000)))))
