def main(a, b, m):
    poly = 1
    for k in range(1, m + 1):
        sum0 = 0
        for j in range(1, b + 1):
            sum1 = 0
            for c in range(1, a + 1):
                sum1 += 79 - (j ** 2 - 12 * k - 1) ** 3 - c ** 6
            sum0 += sum1
        poly *= sum0
    return poly
