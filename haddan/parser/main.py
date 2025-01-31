"""Тестирование api haddan.ru."""
from bs4 import BeautifulSoup
import requests_cache
from requests_html import HTMLSession
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import API_URL, LIBRIARY_URL
from outputs import control_output
from db_utils import Thing, DATABASE_URL


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


def get_user_bool_online(session, username):
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


def get_user_online(session, username):
    """Выводит читабельный ответ в сети юзер или нет."""
    if get_user_bool_online(username):
        print(f'Пользователь {username} в сети.')
    else:
        print(f'Пользователь {username} оффлайн.')


def get_user_wear(session, username):
    """Сохраняет в файл и обновляет в БД весь надетый шмот юзера."""
    url = API_URL + get_user_wear_url(username)
    response = session.get(url)
    root = xml_parser(response)
    result = {}
    place = root.find_all('place')
    # engine = create_engine('sqlite:///haddan.db', echo=False)
    engine = create_engine(DATABASE_URL, echo=False)
    db_session = Session(engine)
    thing_session = HTMLSession()
    for place in tqdm(root.find_all('place')):
        thing_url = LIBRIARY_URL + place.find('thingid').text
        thing_response = thing_session.get(thing_url)
        thing_response.html.render()
        thing_soup = BeautifulSoup(thing_response.html.html, 'lxml')
        thing_name = thing_soup.find('td', {'class': 'description'}).h3.text
        thing_serial_number = int(place.find('thingid').text)
        thing_part_number = int(place.find('thingtypeid').text)
        result[thing_name] = {
            'Тип': place['id'],
            'S/N': thing_serial_number,
            'артикул': thing_part_number,
            'прочность': place.find('durc').text,
            'ссылка': thing_url
        }
        existing_thing = db_session.query(
            Thing).filter_by(
                serial_number=thing_serial_number
                ).first()
        if existing_thing:
            existing_thing.name = thing_name
            existing_thing.type = place['id']
            existing_thing.part_number = thing_part_number
            existing_thing.owner = username
            existing_thing.href = thing_url
        else:
            thing = Thing(
                name=thing_name,
                type=place['id'],
                serial_number=thing_serial_number,
                part_number=thing_part_number,
                owner=username,
                href=thing_url
            )
            db_session.add(thing)
        db_session.commit()
    return result


def get_item_info(session, tid):
    """Сохраняет в txt файл инфо предмета по его SN."""
    url = API_URL + get_wear_info_url(tid)
    root = xml_parser(session.get(url))
    keys = ('typefull', 'thingid', 'thingtypeid', 'name')
    wear_dict = {key: root.find(key).text for key in keys}
    for bon in root.BonusReqs.Bonuses:
        wear_dict[bon['name']] = bon.text
    with open(
        f'wear/item_id/{wear_dict["name"]}_SN={wear_dict["thingid"]}.txt',
        'w',
        encoding='utf-8'
    ) as f:
        for key, value in wear_dict.items():
            f.write(f"{key}: {value}\n")


def item_search(session, name):
    url_name = API_URL + get_item_search_url(name)
    response = session.get(url_name)
    soup = xml_parser(response)
    print(soup)


MODE_TO_FUNCTION = {
    'wear': get_user_wear,
    'item-info': get_item_info,
}


def main():
    configure_logging()
    logging.info('Парсер запущен!')
    try:
        arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
        args = arg_parser.parse_args()
        session = requests_cache.CachedSession()
        if args.clear_cache:
            session.cache.clear()
        parser_mode = args.mode
        results = MODE_TO_FUNCTION[parser_mode](session, args.input)
        if results:
            control_output(results, args)
    except Exception as e:
        logging.exception(
            f'\nВозникло исключение {str(e)}\n',
            stack_info=True
        )
    logging.info('Парсер завершил работу.')


if __name__ == '__main__':
    main()
