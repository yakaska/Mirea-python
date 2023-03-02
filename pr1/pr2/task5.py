def d3(y, z):
    res = []
    for i in range(len(y)):
        res.append(abs(y[i] - z[i]))
    return max(res)


y = (1.0, 0.5, 1.0)
z = (0.5, 2.0, 1.0)
print(d3(y, z))
