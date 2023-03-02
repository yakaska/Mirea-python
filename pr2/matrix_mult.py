from array import array


def matrix_mult(matrix_a, matrix_b):
    
    return matrix_a * matrix_b


matrixA = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
]

matrixB = [
    [2, 0, 0, 0],
    [2, 2, 0, 0],
    [2, 2, 2, 0],
    [2, 2, 2, 2],
]

print(matrix_mult(matrixA, matrixB))
