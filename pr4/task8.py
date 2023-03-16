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


def alg(a, i, j):
    return (-1) ** (i + j) * minor(a, i, j)


def transpose(a):
    return [[row[i] for row in a] for i in range(len(a[0]))]


def alg_matrix(a):
    cofactors = []
    for i in range(len(a)):
        line = []
        for j in range(len(a)):
            cofactor = alg(a, i, j)
            line.append(cofactor)
        cofactors.append(line)
    return cofactors


def reverse(a):
    cofactors = transpose(alg_matrix(a))
    determinant = det(a)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def multiply(x, y):
    return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*y)] for X_row in x]


def moore_penrose(h):
    h_transposed = transpose(h)
    return multiply(
        reverse(multiply(h_transposed, h)),
        h_transposed
    )


A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

print(moore_penrose(A))
