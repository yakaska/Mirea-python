from math import cos


def f(n):
    if n == 0:
        return 6
    elif n == 1:
        return 4
    else:
        return 1 / 45 * (f(n - 2)) ** 3 + cos(f(n - 1))


print(f(12))
