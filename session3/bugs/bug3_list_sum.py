# Find the bug 3: without return the recursive case gives None


def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


print(sum_list([1, 2, 3]))
