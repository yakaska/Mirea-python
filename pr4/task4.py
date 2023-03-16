def small_det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def sub_matrix(a, i, j):
    return [row[:j] + row[j + 1:] for row in (a[:i] + a[i + 1:])]


def det(a, i=0):
    if len(a) == 2:
        return small_det(a)
    determinant = 0
    for j in range(len(a)):
        determinant += (-1) ** (i + j) * a[i][j] * det(sub_matrix(a, i, j))
    return determinant


def minor(a, i, j):
    return det(sub_matrix(a, i, j))


A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

print(minor(A, 0, 1))
