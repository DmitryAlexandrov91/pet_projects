"""Утилитки приложения haddan_miner"""
import re
from time import sleep

from selenium.webdriver.common.by import By

from constants import (FIELD_PRICES, FIRST_CHAR, HADDAN_MAIN_URL,
                       PAGE_SOURCE_PATH, PASSWORD, SECOND_CHAR,
                       TELEGRAM_CHAT_ID)


def send_photo(bot, photo):
    """Отправляет фотку в телеграм."""
    bot.send_photo(TELEGRAM_CHAT_ID, open(photo, 'rb'))


def save_url_content(driver):
    """Сохраняет контент страницы."""
    page_source = driver.page_source
    with open(PAGE_SOURCE_PATH, "w", encoding="utf-8") as file:
        file.write(page_source)


def first_char_login(driver):
    """Вход в игру."""
    username_field = driver.find_element(
        By.NAME, 'username')
    username_field.send_keys(FIRST_CHAR)
    sleep(1)
    password_field = driver.find_element(
        By.NAME, 'passwd')
    password_field.send_keys(PASSWORD)
    sleep(1)
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        '[href="javascript:enterHaddan()"]')
    submit_button.click()


def second_char_login(driver):
    """Вход в игру."""
    username_field = driver.find_element(
        By.NAME, 'username')
    username_field.send_keys(SECOND_CHAR)
    sleep(1)
    password_field = driver.find_element(
        By.NAME, 'passwd')
    password_field.send_keys(PASSWORD)
    sleep(1)
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        '[href="javascript:enterHaddan()"]')
    submit_button.click()


def try_to_switch_to_central_frame(driver):
    """Переключается на центральный фрейм окна."""
    frames = driver.find_elements(By.TAG_NAME, 'iframe')
    if frames:
        for frame in frames:
            if frame.get_attribute('name') == 'frmcenterandchat':
                driver.switch_to.frame("frmcenterandchat")
                driver.switch_to.frame("frmcentral")
                break


def try_to_switch_to_dialog(driver):
    """Переключается на фрейм диалога."""
    frames = driver.find_elements(By.TAG_NAME, 'iframe')
    if frames:
        for frame in frames:
            if frame.get_attribute('id') == 'thedialog':
                driver.switch_to.frame("thedialog")
                break


# def find_kaptcha(driver):
#     driver.switch_to.frame("func")
#     image_element = driver.find_element(
#         By.CSS_SELECTOR,
#         'img[src="/inner/img/gc.php"]')
#     return image_element


def get_kaptcha_answer(message, driver):
    """Отправляет ответ на капчу."""
    button = driver.find_element(
        By.CSS_SELECTOR,
        f'button[value="{message}"]')
    button.click()


def fight(driver):
    """Проводит бой."""
    while driver.find_elements(
                    By.PARTIAL_LINK_TEXT, 'Ударить'):
        hits = driver.find_elements(
            By.CSS_SELECTOR,
            'img[onclick="touchFight();"]')
        if hits:
            hits[0].click()
        sleep(0.5)


def check_kaptcha(driver, bot=None):
    """Проверяет наличие капчи на странице."""
    kaptcha = driver.find_elements(
                By.CSS_SELECTOR,
                'img[src="/inner/img/bc.php"]'
            )
    if kaptcha:
        print('Обнаружена капча!')
        kaptcha[0].screenshot('kaptcha.png')
        sleep(30)
        if bot is not None:
            send_photo(bot, 'kaptcha.png')
            sleep(1)
            send_photo(bot, 'runes.png')
            sleep(30)
    driver.refresh()


def try_to_click_to_glade_fairy(driver):
    """Ищет фею поляны и щёлкает на неё."""
    glade_fairy = driver.find_elements(
                    By.CSS_SELECTOR,
                    'img[id="roomnpc231778"]')
    if not glade_fairy:
        glade_fairy = driver.find_elements(
                    By.CSS_SELECTOR,
                    'img[id="roomnpc17481"]')

    if len(glade_fairy) > 0:
        glade_fairy[0].click()
        sleep(1)


def price_counter(resurses, price_diсt=FIELD_PRICES):
    """Находит самый дорогой ресурс из списка и возвращает его индекс."""
    result = []
    for s in resurses:
        pattern = r'(\D+)\s+-\s+(\d+)'
        match = re.match(pattern, s)
        if match:
            part1 = match.group(1).strip()
            part2 = int(match.group(2))
            result.append(part2 * price_diсt[f'{part1}'])
    return result.index(max(result))


def time_extractor(text):
    """Извлекает время из строки с текстом."""
    pattern = r'-?\d+:\d+'
    matches = re.findall(pattern, text)
    if not matches:
        return 0
    time_str = matches[0]
    minutes, secundes = map(int, time_str.split(':'))
    if minutes >= 0 and secundes >= 0:
        return minutes * 60 + secundes
    return 0


# Блок управления быстрыми слотами
def select_slot(driver):
    """Щёлкает по слоту(по умолчанию выбран слот с эликсирами)"""
    slots = driver.find_element(
                By.CSS_SELECTOR,
                'a[href="javascript:slotsShow(0)"]'
            )
    print(slots)
    slots.click()


def select_spell(driver, spell='0'):
    """Выбирает заклинание(по умолчанию самое первое)"""
    spell = driver.find_elements(
                By.CSS_SELECTOR,
                f'a[id="slot{spell}"]'
            )
    print(spell)
    if spell:
        spell[0].click()


