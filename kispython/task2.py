from math import tan, ceil


def main(y):
    if y < 74:
        return ((y - 74 * y ** 3) ** 5) / 68
    elif 74 <= y < 147:
        return tan(y) ** 7
    elif 147 <= y < 203:
        return 89 * (y ** 3 - y - 63 * y ** 2) ** 2 \
            - (y ** 3 - 21 * y) ** 3 - 21 * (96 * y ** 2 - y ** 3 / 69) ** 4
    elif 203 <= y < 295:
        return ceil(y) - 1 - y ** 2
    elif y >= 295:
        return 29 * (y ** 2 - 1 - y ** 3) ** 4
