# Exercise: transpose a matrix (rows become columns)


def transpose_loops(m):
    result = []
    for c in range(len(m[0])):
        row = []
        for r in range(len(m)):
            row.append(m[r][c])
        result.append(row)
    return result


def transpose(m):
    return [[m[r][c] for r in range(len(m))]
            for c in range(len(m[0]))]


m = [[1, 2, 3],
     [4, 5, 6]]
print(transpose_loops(m))
print(transpose(m))
