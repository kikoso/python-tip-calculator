# Find the bug 3: assigning to count inside the function makes it local
# (UnboundLocalError). Fix: pass the value in and return the new one.


def visit(count):
    return count + 1


count = 0
count = visit(count)
print(count)
