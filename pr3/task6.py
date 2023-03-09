def transcode(int_string):
    int_value = int(int_string)
    s1 = int_value & ((1 << 7) - 1)
    s2 = (int_value >> 7) & ((1 << 3) - 1)
    s3 = (int_value >> 10) & ((1 << 10) - 1)
    s4 = (int_value >> 16) & ((1 << 4) - 1)
    return str(s1 | s3 << 7 | s4 << 13 | s2 << 17)


print(transcode('743096'))
