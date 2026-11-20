# Homework session 3 (challenge): all subsets, recursive. 2^n subsets, O(2^n)


def subsets(items):
    if not items:
        return [[]]
    rest = subsets(items[1:])
    with_first = [[items[0]] + s for s in rest]
    return rest + with_first


result = subsets([1, 2, 3])
print(result)
print(len(result))
