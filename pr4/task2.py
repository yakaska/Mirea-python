def sub_matrix(a, i, j):
    return [row[:j] + row[j + 1:] for row in (a[:i] + a[i + 1:])]


A = [
    [0, 2, 1],
    [1, 4, 3],
    [2, 1, 1]
]

print(sub_matrix(A, 0, 0))
