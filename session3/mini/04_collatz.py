# Mini exercise 4: Collatz steps until 1


def collatz_steps(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz_steps(n // 2)
    return 1 + collatz_steps(3 * n + 1)


print(collatz_steps(6))
print(collatz_steps(27))
