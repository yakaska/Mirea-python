def main(s):
    value = s
    q1 = value & ((1 << 2) - 1)
    q3 = (value >> 5) & ((1 << 8) - 1)
    q4 = (value >> 13) & ((1 << 6) - 1)
    q5 = (value >> 19) & ((1 << 3) - 1)
    q6 = (value >> 22) & ((1 << 5) - 1)
    return str(hex(q3 | q6 << 11 | q5 << 16 | q4 << 19 | q1 << 25))
