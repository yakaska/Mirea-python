def main(a, n, m, y):
    sum1 = 0
    for i in range(1, a + 1):
        sum1 += 11 * (46 * i + 77 * i ** 3) ** 4
    sum2 = 0
    for c in range(1, a + 1):
        poly = 1
        for i in range(1, m + 1):
            sum3 = 0
            for k in range(1, n + 1):
                sum3 += (45 * i - k ** 3 - k ** 2) ** 2 + c ** 7 + 40 * y
            poly *= sum3
        sum2 += poly
    return sum1 + sum2
