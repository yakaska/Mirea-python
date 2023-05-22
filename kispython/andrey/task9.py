import re


def main(table):
    result = []
    re_name = r'(\S+)\s(\S+)\s(\S+)'
    for line in table:
        filtered = list(filter(None, line))
        norm = list(dict.fromkeys(filtered))
        res_row = []

        name, date = norm[0].split('|')

        np = re.findall(re_name, name)[0]
        name = f'{np[0][0]}.{np[1]} {np[2]}'

        dp = [date[0:2], date[3:5], date[6:9]]
        date = f'{dp[2]}/{dp[1]}/{dp[0]}'

        email = norm[1].replace('@', '[at]')

        res_row.extend([name, email, date])
        result.append(res_row)
    result.sort(key=lambda x: x[0])
    return [list(i) for i in zip(*result)]


test_table = [
    ['Родион А. Шотко|04-01-05', 'rodion9@yahoo.com', None, 'rodion9@yahoo.com'],
    ['Кирилл Ф. Загак|01-02-23', 'kirill58@gmail.com', None, 'kirill58@gmail.com'],
    ['Роберт Ш. Мулак|03-11-21', 'robert60@yahoo.com', None, 'robert60@yahoo.com'],
    ['Родион О. Гефак|99-10-11', 'rodion88@mail.ru', None, 'rodion88@mail.ru']
]

res = main(test_table)
for line in res:
    print(line)
