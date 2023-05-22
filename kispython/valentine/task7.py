def main(int_string):
    int_value = int(int_string)
    e2 = int_value >> 9 & 0b0_0_0000_00000_11111
    e3 = int_value >> 14 & 0b0_0_0000_11111
    e4 = int_value >> 19 & 0b0_0_1111
    e5 = int_value >> 23 & 0b0_1
    e6 = int_value >> 24 & 0b1
    return dict(zip(['E2', 'E3', 'E4', 'E5', 'E6'], [e2, e3, e4, e5, e6]))


print(main('18546698'))
