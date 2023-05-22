def main(tup):
    d1 = int(tup[0]) & 0b000000_00000_0_111111
    d2 = int(tup[1]) << 6 & 0b000000_00000_1_000000
    d3 = int(tup[2]) << 7 & 0b000000_11111_0_000000
    return hex(d1 | d2 | d3)


print(main((5, 1, 10)))
print(main((13, 1, 3)))
print(main((51, 1, 17)))
print(main((7, 0, 11)))
