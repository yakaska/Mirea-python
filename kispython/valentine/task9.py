import re


def main(table):
    r_name = r'(\D+) \D. (\D*)'
    r_perc = r'(\d*)%'
    result = []
    for line in table:
        filtered = list(filter(None, line))
        norm = list(dict.fromkeys(filtered))
        norm[0] = f"{(int(re.search(r_perc, norm[0]).group(1)) / 100):.2f}"
        norm[1] = norm[1][4::]
        norm[2] = "Да" if norm[2] == "Y" else "Нет"
        norm[3] = " ".join(re.findall(r_name, norm[3])[0])
        result.append(norm)
    return [list(i) for i in zip(*result)]


test_table_1 = [
    ['12%', None, '197-151-7150', None, 'N', 'Петр О. Гуцак', 'N'],
    ['13%', None, '256-323-3474', None, 'Y', 'Яромир Р. Тагусский', 'Y'],
    ['8%', None, '107-606-1052', None, 'N', 'Мирослав Т. Сишосов', 'N']
]

test_table_2 = [
    ['89%', None, '550-988-2110', None, 'N', 'Игнат Б. Фачобий', 'N'],
    ['51%', None, '494-350-8610', None, 'Y', 'Михаил Ч. Тилафман', 'Y'],
    ['54%', None, '001-106-0220', None, 'Y', 'Анатолий К. Шецян', 'Y']
]

test_table_3 = [
    ['60%', None, '735-189-6143', None, 'N', 'Богдан Р. Гукивяк', 'N'],
    ['19%', None, '646-795-6013', None, 'Y', 'Даниил С. Фебучий', 'Y'],
    ['82%', None, '693-148-6482', None, 'N', 'Даниил А. Фузозак', 'N']
]


tables = [test_table_1, test_table_2, test_table_3]

for i in range(len(tables)):
    tables[i] = main(tables[i])


for table in tables:
    for line in table:
        print(line)
    print()
