"""Утилитки парсеров."""


# spar.py
def text_formatter(text: str):
    """Убирает из текста символ переноса строки."""
    if '\n' in text:
        new_text = text.replace('\n', ' ')
        return new_text
    return text


def price_formatter(text):
    """Форматирует строку в читабельный формат цены."""
    formatted_text = text_formatter(text)
    splitted_text = formatted_text.split()
    upd_price = splitted_text[0][:-2] + '.' + splitted_text[0][-2:]
    splitted_text[0] = upd_price
    return ' '.join(splitted_text)


def list_combiner(products: list, prices: list) -> dict:
    """Объединяет два списка в словарь ключ: значение."""
    results = {}
    for idx, product in enumerate(products):
        try:
            results[product] = prices[idx]
        except Exception as e:
            print(f'Распакоука пошла не по плану! {e}')
            return results
    return results
# да, тут можно использовать dict(zip(products, prices)),
# но как тогда ловить исключение и возвращать неполный словарь?
