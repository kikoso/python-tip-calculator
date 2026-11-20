# Find the bug 1: [["."] * 3] * 3 repeats one row. Build each row separately
board = [["."] * 3 for _ in range(3)]
board[1][1] = "X"
for row in board:
    print(row)
