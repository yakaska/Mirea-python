def d4(y, z):
    res = 0
    for i in range(len(y)):
        res += (y[i] - z[i]) ** 2
    return res


y = (1.0, 0.5, 1.0)
z = (0.5, 2.0, 1.0)
print(d4(y, z))
