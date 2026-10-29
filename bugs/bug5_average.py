# Find the bug 5: the average grade
# Bug: without brackets Python calculates c / 3 first (precedence).

a = 1.0
b = 2.0
c = 3.0
average = (a + b + c) / 3
print(average)
