def transcode(int_string):
    int_value = int(int_string)
    s1 = int_value & ((1 << 3) - 1)
    s2 = (int_value >> 3) & ((1 << 4) - 1)
    s4 = (int_value >> 17) & ((1 << 10) - 1)
    s5 = (int_value >> 27) & ((1 << 11) - 1)
    return str(hex(s4 | s1 << 20 | s5 << 23 | s2 << 33))


print(transcode('239948252'))
