import re


def main(table):
    regex_name = r'(\D+) \D. (\D*)'
    regex_percentage = r'(\d*)%'
    result = []
    for line in table:
        filtered = list(filter(None, line))
        removed_duplicates = list(dict.fromkeys(filtered))
        removed_duplicates[0] = str(int(re.search(
            regex_percentage, removed_duplicates[0]).group(1)) / 100)
        removed_duplicates[1] = removed_duplicates[1][4::]
        removed_duplicates[2] = "Да" if removed_duplicates[2] == "Y" else "Нет"
        removed_duplicates[3] = " ".join(re.findall(
            regex_name, removed_duplicates[3])[0])
        result.append(removed_duplicates)
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

print(main(test_table_1))
print(main(test_table_2))
