def matrix_transpon_one_line(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix))]


def matrix_transpon(matrix):
    transpon = []
    for i in range(len(matrix)):
        transp_row = []
        for row in matrix:
            transp_row.append(row[i])
        transpon.append(transp_row)
    return transpon


matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

print(matrix_transpon(matrix))
print(matrix_transpon_one_line(matrix))
