from math import ceil


def main(x, z, y):
    sum0 = 0
    n = len(x)
    for i in range(1, n + 1):
        a = y[n - ceil(i / 2)]
        b = z[n - i]
        c = x[ceil(i / 3) - 1]
        sum0 += 95 * (3 * a ** 2 - 33 * b - 27 * c ** 3) ** 6
    return 72 * sum0
