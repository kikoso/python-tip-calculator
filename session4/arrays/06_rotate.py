# Exercise: rotate a list k places to the right with slicing


def rotate(lst, k):
    if not lst:
        return []
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(rotate([1, 2, 3, 4, 5], 2))
print(rotate([1, 2, 3, 4, 5], 7))
print(rotate([1, 2, 3], 0))
