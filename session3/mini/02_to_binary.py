# Mini exercise 2: binary representation, recursive


def to_binary(n):
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


print(to_binary(13))
print(to_binary(1))
