def main(n):
    if n == 0:
        return 0.94
    elif n == 1:
        return -0.62
    elif n >= 2:
        return 38 * main(n - 2) + 1 + main(n - 1)
