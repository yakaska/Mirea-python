def find(seq, find):
    return [i for i, x in enumerate(seq) if x == find]


print(find([1, 1, 1, 1, 1, 22, 2, 3], 1))
