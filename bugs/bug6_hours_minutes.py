# Find the bug 6: hours and minutes
# Bug: / always gives a float (2.25). // gives the whole hours (2).

minutes = 135
hours = minutes // 60
rest = minutes % 60
print(f"{hours} Std. {rest} Min.")
