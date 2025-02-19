from constants import FIELD_PRICES
import re 

resurses_list = [
    'Зеленая массивка - 5 шт.',
    'Мухожор - 34 шт.',
    'Подсолнух - 15 шт.',
    'Капустница - 9 шт.',
    'Мандрагора - 8 шт.',
    'Колючник Черный - 2 шт.',
    'Гертаниум - 1 шт.'
]


def price_counter(resurses):
    result = []
    for s in resurses:
        pattern = r'(\D+)\s+-\s+(\d+)'
        match = re.match(pattern, s)
        if match:
            part1 = match.group(1).strip()
            part2 = int(match.group(2))
            result.append(part2 * FIELD_PRICES[f'{part1}'])
    most_cheep_res = result.index(max(result))
    return most_cheep_res


