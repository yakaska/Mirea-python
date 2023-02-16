import timeit
from Levenshtein import distance as lev


def f(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return f(a, b, i - 1, j - 1)
    else:
        return 1 + min(f(a, b, i, j - 1), f(a, b, i - 1, j), f(a, b, i - 1, j - 1))


# a = 'Hello, world!'
# b = 'Goodbye, world!'
# print(f(a, b, len(a), len(b)))

my_lev = '''def f(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return f(a, b, i - 1, j - 1)
    else:
        return 1 + min(f(a, b, i, j - 1), f(a, b, i - 1, j), f(a, b, i - 1, j - 1))
    
a = 'Hello, world!'
b = 'Goodbye, world!'
f(a, b, len(a), len(b))'''

test_lev = '''
def test(a, b):
    return lev(a, b)


a = 'Hello, world!'
b = 'Goodbye, world!'
'''

print(min(timeit.Timer(stmt=my_lev).repeat(7, 100)))
print(min(timeit.Timer(stmt=test_lev, setup="from Levenshtein import distance as lev").repeat(7, 100)))
# print(timeit.repeat(stmt=test_lev, setup="from Levenshtein import distance as lev", number=1_000_000))
