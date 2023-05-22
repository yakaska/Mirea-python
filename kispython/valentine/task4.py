def main(n):
    if n == 0:
        return -0.44
    elif n >= 1:
        return main(n - 1) ** 6 + main(n - 1) + 0.01
