def main(s):
    value = int(s)
    m1 = value & ((1 << 8) - 1)
    m2 = (value >> 8) & ((1 << 9) - 1)
    m3 = (value >> 9) & ((1 << 9) - 1)
    m4 = (value >> 18) & ((1 << 2) - 1)
    m5 = (value >> 20) & ((1 << 2) - 1)
    m6 = (value >> 22) & ((1 << 5) - 1)
    return str(hex(m5 | m4 << 2 | m6 << 4 | m1 << 9 | m2 << 17 | m3 << 18))
