def count_characters(words):
    words = words.lower()
    res = {}
    for c in words:
        res[c] = f(words, c)
    return res


def f(s, c):
    count = 0
    for i in range(len(s)):
        if s[i] == c:
            count += 1
    return count


print(count_characters('I love the Python programming language!'))
