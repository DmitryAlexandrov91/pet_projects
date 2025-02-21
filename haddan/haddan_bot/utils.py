"""Утилитки приложения haddan_miner"""
from time import sleep
import re

from selenium.webdriver.common.by import By

from constants import (FIELD_PRICES, FIRST_CHAR, HADDAN_MAIN_URL, PAGE_SOURCE_PATH, PASSWORD,
                       SECOND_CHAR, TELEGRAM_CHAT_ID)


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


def get_temple_kaptcha(driver):
    """Возвращает картинку  капчей из храма."""
    # Переключаемся в комнату копки.
    driver.switch_to.frame("frmcenterandchat")
    driver.switch_to.frame("frmcentral")
    # Нажимаем кнопку медитация.
    meditation_link = driver.find_element(By.LINK_TEXT, "медитация")
    meditation_link.click()
    sleep(1)
    # Переключаемся на фрейм с медитацией
    driver.switch_to.frame("func")
    # Находим капчу и отправляем в телеграм
    image_element = driver.find_element(
        By.CSS_SELECTOR,
        'img[src="/inner/img/gc.php"]')
    if image_element:
        return image_element


def get_mine_kaptcha(driver):
    """Возвращает картинку  капчей из храма."""
    # Переключаемся в комнату медатации.
    driver.switch_to.frame("frmcenterandchat")
    driver.switch_to.frame("frmcentral")
    # Нажимаем кнопку Копать.
    mine_link = driver.find_element(By.LINK_TEXT, "Копать")
    mine_link.click()
    sleep(1)
    # Переключаемся на фрейм с копкой
    driver.switch_to.frame("func")
    # Находим капчу и отправляем в телеграм
    image_element = driver.find_element(
        By.CSS_SELECTOR,
        'img[src="/inner/img/gc.php"]')
    if image_element:
        return image_element


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
    frames = driver.find_elements(By.TAG_NAME, 'iframe')
    if frames:
        for frame in frames:
            if frame.get_attribute('id') == 'thedialog':
                driver.switch_to.frame("thedialog")
                break


# def try_to_find_kaptcha(driver):


def find_kaptcha(driver):
    driver.switch_to.frame("func")
    image_element = driver.find_element(
        By.CSS_SELECTOR,
        'img[src="/inner/img/gc.php"]')
    return image_element


def get_kaptcha_answer(message, driver):
    """Отправляет ответ на капчу."""
    button = driver.find_element(
        By.CSS_SELECTOR,
        f'button[value="{message}"]')
    button.click()


def price_counter(resurses, price_dit=FIELD_PRICES):
    """Находит самый дорогой ресурс из списка."""
    result = []
    for s in resurses:
        pattern = r'(\D+)\s+-\s+(\d+)'
        match = re.match(pattern, s)
        if match:
            part1 = match.group(1).strip()
            part2 = int(match.group(2))
            result.append(part2 * price_dit[f'{part1}'])
    most_cheep_res = result.index(max(result))
    return most_cheep_res


def time_extractor(text):
    """Извлекает время из строки с текстом."""
    pattern = r'-?\d+:\d+'
    matches = re.findall(pattern, text)
    if matches:
        time_str = matches[0]
        minutes, secundes = map(int, time_str.split(':'))
        if minutes >= 0 and secundes >= 0:
            return minutes * 60 + secundes
        return 0
    return 0


class HaddanBot():

    """Бот класс управления действий персонажа.

    Принимает два обязательных аргумента при инициализации:
        char - никнейм персонажа,
        driver - экземпляр класса  webdriver.Chrome.

    """

    def __init__(self, char, driver, bot=None):
        self.driver = driver
        self.char = char
        if bot is not None:
            self.bot = bot

    def login_to_game(self, password):
        """Заходит в игру под заданным именем char."""
        self.driver.get(HADDAN_MAIN_URL)
        self.driver.maximize_window()
        sleep(1)
        username_field = self.driver.find_element(
            By.NAME, 'username')
        username_field.send_keys(self.char)
        sleep(1)
        password_field = self.driver.find_element(
            By.NAME, 'passwd')
        password_field.send_keys(password)
        sleep(1)
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR,
            '[href="javascript:enterHaddan()"]')
        submit_button.click()
        sleep(4)

    def save_page_content(self):
        """Сохраняет HTML код страницы в файл."""
        page_source = self.driver.page_source
        with open(PAGE_SOURCE_PATH, "w", encoding="utf-8") as file:
            file.write(page_source)

    def switch_to_central_frame(self):
        """Переключается на центральный фрейм окна."""
        self.driver.switch_to.frame("frmcenterandchat")
        self.driver.switch_to.frame("frmcentral")

    def click_to_glade_fairy(self):
        """Начать диалог с феей поляны."""
        glade_fairy = self.driver.find_element(
            By.CSS_SELECTOR,
            'img[id="roomnpc231778"]')
        glade_fairy.click()

    def start_farm_herbs(self):
        """Кликает на вариант ответа "Да, мне нужны новые травы"."""
        self.driver.switch_to.frame("thedialog")
        battle_start = self.driver.find_element(
            By.CLASS_NAME,
            'talksayTak')
        battle_start.click()
        if self.driver.find_element(
            By.CLASS_NAME,
            'talksayTak'
        ):
            confirm = self.driver.find_element(
                By.CLASS_NAME,
                'talksayTak')
            confirm.click()

    def battle(self):
        """Автобой (тыкает на изображение npc пока бой не закончится)."""
        while self.driver.find_element(
                By.PARTIAL_LINK_TEXT, 'Ударить'
                ):
            hit = self.driver.find_element(
                By.CSS_SELECTOR,
                'img[onclick="touchFight();"]')
            hit.click()
            sleep(1)
