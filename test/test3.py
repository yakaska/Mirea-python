def get_start_with(words, c):
    return [word for word in words if word.lower()[0] == c.lower()]


words = ['print', 'nice', 'nutella', 'spring', 'natsu', 'python', 'mouse']
c = 'p'

print(get_start_with(words, c))
print(get_start_with(words, c.upper()))
