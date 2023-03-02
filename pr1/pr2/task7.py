def d5(y, z, h=5):
    res = 0
    for i in range(len(y)):
        res += abs(y[i] - z[i]) ** h
    return res ** (1 / h)


y = (1.0, 0.5, 1.0)
z = (0.5, 2.0, 1.0)
h = 5
print(d5(y, z, h))
