def main(input_table):
    # Удаление дубликатов по столбцам
    input_table = [list(x) for x in zip(*input_table)]
    normalized = []
    seen_columns = set()
    for i, column in enumerate(input_table):
        if column[0] not in seen_columns:
            seen_columns.add(column[0])
            normalized.append(column)
    normalized = [list(x) for x in zip(*normalized)]
    # Удаление дубликатов по строкам
    seen_rows = set()
    index_to_remove = []
    for i, row in enumerate(normalized):
        row_tuple = tuple(row)
        if row_tuple not in seen_rows:
            seen_rows.add(row_tuple)
        else:
            index_to_remove.append(i)

    for index in reversed(index_to_remove):
        normalized.pop(index)

    result = []
    for row in normalized:
        result_row = []
        # Преобразование номера телефона
        number = row[0]
        number_parts = [
            number[:2],
            number[3:6],
            number[7:10],
            number[11:13],
            number[13:15]
        ]
        number = "{} ({}) {}-{}-{}".format(*number_parts)
        row[0] = number

        # Преобразование даты и почты
        date, email = row[1].split('!')

        # Преобразование даты
        date_parts = [date[2:4], date[5:7], date[8:10]]
        date = f'{date_parts[0]}-{date_parts[1]}-{date_parts[2]}'

        # Преобразование email
        email = email.replace("[at]", "@")

        # Преобразование имени
        name = row[2]
        last_name = name.split()[0]
        name = last_name

        result_row.extend([number, date, email, name])
        result.append(result_row)

    return result


test_table = [
    ['+7 449 049-3902', '1999.07.25!kasuvuk86[at]gmail.com', 'Кашувук В.У.', 'Кашувук В.У.'],
    ['+7 017 960-0918', '2002.08.20!cuzin51[at]gmail.com', 'Чузин С.И.', 'Чузин С.И.'],
    ['+7 017 960-0918', '2002.08.20!cuzin51[at]gmail.com', 'Чузин С.И.', 'Чузин С.И.'],
    ['+7 017 960-0918', '2002.08.20!cuzin51[at]gmail.com', 'Чузин С.И.', 'Чузин С.И.'],
    ['+7 517 790-8955', '2004.06.07!sulli39[at]mail.ru', 'Шулли С.Л.', 'Шулли С.Л.'],
]

res = main(test_table)
for line in res:
    print(line)
