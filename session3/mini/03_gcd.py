# Mini exercise 3: greatest common divisor (Euclid)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(48, 18))
print(gcd(17, 5))
