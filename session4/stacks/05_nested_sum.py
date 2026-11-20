# Recursion replaced by an explicit stack


def nested_sum_recursive(data):
    total = 0
    for x in data:
        if isinstance(x, list):
            total += nested_sum_recursive(x)
        else:
            total += x
    return total


def nested_sum(data):
    total = 0
    stack = [data]
    while stack:
        for x in stack.pop():
            if isinstance(x, list):
                stack.append(x)
            else:
                total += x
    return total


data = [1, [2, [3, 4]], 5]
print(nested_sum_recursive(data))
print(nested_sum(data))
