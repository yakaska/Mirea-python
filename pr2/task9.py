from itertools import groupby


def rle_encode(string):
    return [(k, sum(1 for _ in g)) for k, g in groupby(string)]


print(rle_encode('wwweeerrrttt'))
