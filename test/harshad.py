def harshad(n):
    d_sum = 0
    copy_n = n
    while n != 0:
        d = n % 10
        d_sum += d
        n = int(n / 10)
    return copy_n % d_sum == 0


print(harshad(155))
