"""Тестирование api haddan.ru."""
import requests
import xml.etree.ElementTree as ET


API_URL = 'https://haddan.ru/inner/api.php'


def xml_parser(response):
    """Парсер для обработки методом find."""
    root = ET.fromstring(response.text)
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


def get_user_bool_online(username):
    """Возвращает True если пользователь в сети."""
    url = API_URL + get_username_online_url(username)
    response = requests.get(url)
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
    response = requests.get(url)
    root = xml_parser(response)
    data_dict = {}
    for place in root.findall('.//place'):
        data_dict[place.attrib['id']] = {
            'thingid': place.find('thingid').text,
            'thingtypeid': place.find('thingtypeid').text,
            'durc': place.find('durc').text,
        }
    with open(f'wear/user_wear/{username}_wear.xml', 'w') as f:
        for key, value in data_dict.items():
            f.write(f"{key}: {value}\n")


def get_wear_info(tid):
    """Сохраняет в xml файл полную инфо о вещи по её SN."""
    url = API_URL + get_wear_info_url(tid)
    root = xml_parser(requests.get(url))
    bonuses = root.find('BonusReqs')
    keys = ('typefull', 'thingid', 'thingtypeid', 'name')
    wear_dict = {key: root.find(key).text for key in keys}
    for req in bonuses.findall('./Requirments/Req'):
        wear_dict[f'{req.attrib["name"]}'] = req.text
    for req in bonuses.findall('./Bonuses/Bon'):
        wear_dict[f'{req.attrib["name"]}'] = req.text
    try:
        with open(
            f'wear/wear_id/{wear_dict["name"]}_SN={wear_dict["thingid"]}.xml',
            'w',
            encoding='utf-8'
        ) as f:
            for key, value in wear_dict.items():
                f.write(f"{key}: {value}\n")
    except Exception:
        with open(
            f'wear/wear_id/{wear_dict["name"]}_SN_недоступен.xml',
            'w',
            encoding='utf-8'
        ) as f:
            for key, value in wear_dict.items():
                f.write(f"{key}: {value}\n")


get_wear_info('15575183')
