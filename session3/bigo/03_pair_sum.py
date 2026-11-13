# Are there two numbers that add up to target?


def has_pair_sum_slow(numbers, target):
    """O(n^2): check all pairs."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False


def has_pair_sum(numbers, target):
    """O(n): remember what we have seen in a set."""
    seen = set()
    for x in numbers:
        if target - x in seen:
            return True
        seen.add(x)
    return False


print(has_pair_sum_slow([3, 8, 1, 5], 9))
print(has_pair_sum([3, 8, 1, 5], 9))
print(has_pair_sum([3, 8, 1, 5], 20))
