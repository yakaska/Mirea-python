import math


def main(y):
    if y < 76:
        a = 30 * (y ** 0.5) ** 4
        b = 19 * (60 - y ** 2) ** 7
        c = 19 * (((y ** 3) / 7) + 0.01 + y)
        return a + b + c
    if 76 <= y < 164:
        return (math.log10(y ** 3)) ** 7
    if 164 <= y < 198:
        return math.ceil(y) ** 3
    if y >= 198:
        a = 4 * y + 59 * y ** 2 + 46 * y ** 3
        return 38 * a ** 6
