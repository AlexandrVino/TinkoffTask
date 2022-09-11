import json


def prepare_data_to_write(data: dict) -> tuple[dict, list]:

    new_data = {}

    for key, value in data.items():
        new_data[key] = sorted(map(lambda x: [x[0], (x[1] * len(x[0]) * 100)], value.items()), key=lambda x: -x[1])
    return new_data, list(data.keys())


def load_data(file_name: str = 'data.json') -> dict | list:
    with open(file_name, 'r', encoding='utf8') as f:
        return json.loads(f.read())


def write_data(file_name: str = 'data.json', file_name_words: str = 'words.json', data: dict = {}) -> None:
    data, words = prepare_data_to_write(data)

    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    with open(file_name_words, 'w', encoding='utf8') as f:
        json.dump(words, f, indent=4, ensure_ascii=False)
