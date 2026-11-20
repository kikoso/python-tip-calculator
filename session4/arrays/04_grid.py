# Two-dimensional lists and the [[0] * 3] * 3 pitfall
rows, cols = 3, 4
grid = [[0] * cols for _ in range(rows)]
grid[1][2] = 5
for row in grid:
    print(row)

wrong = [[0] * 3] * 3
wrong[0][0] = 1
print(wrong)

right = [[0] * 3 for _ in range(3)]
right[0][0] = 1
print(right)
