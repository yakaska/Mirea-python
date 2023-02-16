from math import ceil


def f(n, m):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res += ceil(i) - 76 * j
    temp = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp += 42 * j + 90 * j ** 4 - 80
    temp /= 31
    return 22 * res - temp


print(f(88, 80))