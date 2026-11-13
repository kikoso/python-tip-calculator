# Flatten a list that is nested to any depth


def flatten(items):
    result = []
    for x in items:
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result


print(flatten([1, [2, [3, 4]], 5]))
