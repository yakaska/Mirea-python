import math
import random

file_surnames = r'C:\Users\valen\PycharmProjects\Mirea-python\pr2\homework\namegen\lastnames.txt'
file_names = r'C:\Users\valen\PycharmProjects\Mirea-python\pr2\homework\namegen\names.txt'


def generate_surname():
    surnames = random.sample(list(open(file_surnames, encoding="UTF-8")), k=2)
    surname1 = surnames[0].strip()
    surname2 = surnames[1].strip()
    return surname1[:get_middle_index(surname1):] + surname2[get_middle_index(surname2)::]


def generate_full_name():
    name = random.choice(list(open(file_names, encoding="UTF-8"))).strip()
    initial = random.choice('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    surname = generate_surname()
    return f"{name} {initial}. {surname}"


def get_middle_index(s):
    return math.floor(len(s) / 2)


print(generate_full_name())
