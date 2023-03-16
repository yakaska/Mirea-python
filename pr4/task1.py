def small_det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


A = [[2, 1], [1, 1]]
print(small_det(A))
