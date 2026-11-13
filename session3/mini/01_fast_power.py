# Mini exercise 1: fast power in O(log exp)


def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base


print(fast_power(2, 10))
print(len(str(fast_power(3, 1000))))
