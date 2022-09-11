import os

from education.text_analiser import analise_text
from utils import load_data, write_data


def main():

    path = os.getcwd()

    data = load_data(file_name=f'{path}/data/data.json')
    analise_text(data=data, file_dirname=f'{path}/education/Texts/')
    write_data(data=data, file_name=f'{path}/data/data.json', file_name_words=f'{path}/data/words.json')
    print('ANALISE')


if __name__ == '__main__':
    main()
