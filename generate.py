import os
import random

from utils import load_data
from configargparse import ArgumentDefaultsHelpFormatter, ArgumentParser

PATH = os.getcwd()
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)

parser.add_argument('--length', type=int, default=45, help='Text length')
parser.add_argument('--prefix', type=str, help='Start word')
parser.add_argument('--model', type=str)


def get_data():
    return load_data(file_name='data/data.json'), load_data(file_name='data/words.json')


def get_word(words):
    word = random.choice(words)
    while len(word.split()) != 1:
        word = random.choice(words)

    return word


def main():
    args = parser.parse_args()

    k = args.length
    n = 3

    data, words = get_data()
    if not args.prefix:
        word = get_word(words)
    else:
        word = args.prefix.lower().strip()

    text = generate([word], k, n, data)
    while text == -1:
        word = get_word(words)
        text = generate([word], k, n, data)

    print(text)


def generate(text, k, n, data):
    count = 0
    last_len = len(text)

    while len(text) < k:

        if last_len == len(text):
            count += 1
        else:
            last_len = len(text)

        for i in range(n + 1, 0, -1):

            val = ' '.join(text[-i:])
            data_val = data.get(val)

            if data_val:
                text.append(random.choice(data_val)[0])
                break

        if count > 1000:
            return -1

    return ' '.join(text)


if __name__ == '__main__':
    main()
