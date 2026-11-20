# Find the bug 6: assignment is not a copy. Use copy()
scores = [70, 85, 90]
backup = scores.copy()
scores.append(99)
print("Backup:", backup)
