import random

import pandas as pd


def generate_text(paragraph_count=3):
    table_df = pd.read_html(r'C:\Users\valen\PycharmProjects\Mirea-python\pr2\homework\textgen\table.html')
    table = table_df[0]
    correct_start_index = 0
    text = ''
    for _ in range(paragraph_count):  # text
        for _ in range(3):  # paragraph
            paragraph = table.get('1')[correct_start_index] + ' '
            for j in range(2, 6):  # sentence
                paragraph = paragraph + table.get(str(j))[random.choice(range(8))] + ' '
            text = text + paragraph + '\n'
            correct_start_index = random.choice(range(1, 8))
        text += '\n'
    return text


print(generate_text(paragraph_count=10))
