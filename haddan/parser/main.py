"""Тестирование api haddan.ru."""
from config import configure_argument_parser
import requests_cache
from bs4 import BeautifulSoup


API_URL = 'https://haddan.ru/inner/api.php'
LIBRIARY_URL = 'https://www.haddan.ru/thing.php?id='

session = requests_cache.CachedSession()


def xml_parser(response):
    """Парсер для обработки методом find."""
    root = BeautifulSoup(response.text, features='xml')
    return root


def get_username_online_url(username):
    """Формирует url на онлайн юзера."""
    return f'?op=user&name={username}&fields=online'


def get_user_wear_url(username):
    """Формирует url на обвес юзера."""
    url = f'?op=user&name={username}&fields=wear'
    return url


def get_wear_info_url(tid):
    """Формирует url на инфо об артикуле."""
    url = f'?op=thing&tid={tid}&fields=all'
    return url


def get_item_search_url(name):
    """Формирует url на инфо предмета по имени."""
    url = f'?op=thing&name={name}&fields=all'
    return url


def get_user_bool_online(username):
    """Возвращает True если пользователь в сети."""
    url = API_URL + get_username_online_url(username)
    response = session.get(url)
    try:
        online_value = xml_parser(response).find('online').text
        if online_value == '1':
            return True
        else:
            return False
    except AttributeError:
        print('30 секунд с предыдущего запроса ещё не прошли.')
        exit()


def get_user_online(username):
    """Выводит читабельный ответ в сети юзер или нет."""
    if get_user_bool_online(username):
        print(f'Пользователь {username} в сети.')
    else:
        print(f'Пользователь {username} оффлайн.')


def get_user_wear(username):
    """Сохраняет в файл весь надетый шмот юзера."""
    url = API_URL + get_user_wear_url(username)
    response = session.get(url)
    root = xml_parser(response)
    data_dict = {}
    place = root.find_all('place')
    for place in root.find_all('place'):
        data_dict[place['id']] = {
            'S/N': place.find('thingid').text,
            'артикул': place.find('thingtypeid').text,
            'прочность': place.find('durc').text,
            'ссылка': LIBRIARY_URL + place.find('thingid').text

        }
    with open(f'wear/user_wear/{username}_wear.txt', 'w', encoding='utf-8') as f:
        for key, value in data_dict.items():
            f.write(f"{key}: {value}\n")


def get_wear_info(tid):
    """Сохраняет в xml файл полную инфо о вещи по её SN."""
    url = API_URL + get_wear_info_url(tid)
    root = xml_parser(session.get(url))
    keys = ('typefull', 'thingid', 'thingtypeid', 'name')
    wear_dict = {key: root.find(key).text for key in keys}
    for bon in root.BonusReqs.Bonuses:
        wear_dict[bon['name']] = bon.text
    with open(
        f'wear/wear_id/{wear_dict["name"]}_SN={wear_dict["thingid"]}.xml',
        'w',
        encoding='utf-8'
    ) as f:
        for key, value in wear_dict.items():
            f.write(f"{key}: {value}\n")


def item_search(name):
    url_name = API_URL + get_item_search_url(name)
    response = session.get(url_name)
    soup = xml_parser(response)
    print(soup)


MODE_TO_FUNCTION = {
    'user-wear': get_user_wear,
    'item-info': get_wear_info,
}


def main():
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    session = requests_cache.CachedSession()
    if args.clear_cache:
        session.cache.clear()
    parser_mode = args.mode
    MODE_TO_FUNCTION[parser_mode](args.input)


if __name__ == '__main__':
    main()
