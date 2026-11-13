# Find the bug 1: the base case must also stop the recursion (return)


def countdown(n):
    if n == 0:
        print("Start!")
        return
    print(n)
    countdown(n - 1)


countdown(3)
