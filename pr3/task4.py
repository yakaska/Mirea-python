def decode(hex_string):
    int_value = int(hex_string, 16)
    n1 = int_value & 0b000_00_0000000_000000_111111
    n2 = int_value >> 6 & 0b000_00_0000000_111111
    n3 = int_value >> 12 & 0b000_00_1111111
    n4 = int_value >> 19 & 0b000_11
    n5 = int_value >> 21 & 0b111
    return dict(zip(['n1', 'n2', 'n3', 'n4', 'n5'], [n1, n2, n3, n4, n5]))


print(decode('0xb9a562'))
