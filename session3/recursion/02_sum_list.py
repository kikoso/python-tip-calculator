# Sum of a list, recursive: first element plus the sum of the rest


def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


print(sum_list([4, 8, 15]))
print(sum_list([]))
