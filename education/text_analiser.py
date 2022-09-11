import os
import sys


def prepare_text(text) -> list:
    text = list(' '.join(text.lower().split()))
    for i, value in enumerate(text):
        if value not in 'йцукенгшщзхъфывапролджэячсмитьбю ':
            text[i] = ''

    return ''.join(text).split()


def load_text(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf8') as f:
        return prepare_text(f.read())


def analise_text(text, text_len, data, n):
    for i in range(text_len - 1):

        keys = [' '.join(tuple(text[i:k + 1])) for k in range(i, i + n)]
        values = [text[i + k + 1] for k in range(i, i + n) if i + k + 1 < text_len]

        for key, value in zip(keys, values):

            if not data.get(key): data[key] = {}
            if not data[key].get(value): data[key][value] = 0

            data[key][value] += 1


def wrapper(data: dict, file_dirname: str = None, n=4):

    if file_dirname:

        for file_name in os.listdir(file_dirname):
            print(f'Texts/{file_name}')

            text = load_text(f'{file_dirname}/{file_name}')
            text_len = len(text)

            analise_text(text, text_len, data, n)

    else:
        for line in sys.stdin:
            analise_text(line, len(line), data, n)
