import random
import string


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


print(random_string(10))
print(random_string(100))
