import os

from education.text_analiser import wrapper
from utils import load_data, write_data
from configargparse import ArgumentDefaultsHelpFormatter, ArgumentParser

PATH = os.getcwd()
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '--input-dir', type=str, default=None,
    help='Directory with education texts',
)
parser.add_argument('--model', type=str)


def main():
    args = parser.parse_args()
    file_dirname = args.input_dir

    data = load_data(file_name=f'{PATH}/data/data.json')
    wrapper(data=data, file_dirname=file_dirname)
    write_data(data=data, file_name=f'{PATH}/data/data.json', file_name_words=f'{PATH}/data/words.json')
    print('ANALISE')


if __name__ == '__main__':
    main()
