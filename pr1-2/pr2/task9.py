def reverse(words):
    res = ''
    for word in words[::-1]:
        res += ' ' + word
    return res[1::]


words = ["language!", "programming", "Python", "the", "love", "I"]
print(reverse(words))
