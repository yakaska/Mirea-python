def decode(hex_string):
    int_value = int(hex_string, 16)
    r1 = int_value & 0b000000_000_000_000000000_1111
    r2 = int_value >> 4 & 0b000000_000_000_111111111
    r3 = int_value >> 13 & 0b000000_000_111
    r4 = int_value >> 16 & 0b000000_111
    r5 = int_value >> 19 & 0b111111
    return list(zip(['r1', 'r2', 'r3', 'r4', 'r5'], [r1, r2, r3, r4, r5]))


print(decode('0x6a9f6'))
