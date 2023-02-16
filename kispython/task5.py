def main(x):
    res = 0
    n = len(x)
    for i in range(len(x)):
        res += (21 * x[n - 1 - i] + x[n - 1 - i] ** 2) ** 6
    return res
