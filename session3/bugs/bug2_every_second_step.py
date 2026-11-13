# Find the bug 2: with odd numbers n == 0 is never reached. Use n <= 0.


def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 2)


countdown(5)
