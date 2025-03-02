"""Классы управления работой бота.

DriverManager - класс управления объектом webdriver
HaddanBot  - класс управления действиями персонажа.
"""
import threading
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from constants import (FIELD_PRICES, HADDAN_MAIN_URL, TELEGRAM_CHAT_ID,
                       TIME_FORMAT)
from utils import price_counter, time_extractor


class DriverManager:
    """Класс управления объектом driver."""

    def __init__(self):
        self.driver = None
        self.thread = None
        self.options = webdriver.ChromeOptions()
        self.bot = None

    def start_driver(self):
        """Создаёт объект класса webdriver учитывая self.options."""
        if self.driver is None or self.driver.session_id is None:
            service = Service(executable_path=ChromeDriverManager().install())
            self.driver = webdriver.Chrome(
                service=service,
                options=self.options)
            self.thread = threading.current_thread()

    def close_driver(self):
        """Закрывает активный driver если таковой имеется."""
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
            self.thread = None

    def get_active_driver(self):
        """Функция для проверки наличия активного драйвера."""
        return self.driver

    def save_url_content(self):
        """Сохраняет контент страницы.

        В файле page.html в корне проекта.
        """
        page_source = self.driver.page_source
        with open('page.html', "w", encoding="utf-8") as file:
            file.write(page_source)

    def try_to_switch_to_central_frame(self):
        """Переключается на центральный фрейм окна."""
        frames = self.driver.find_elements(By.TAG_NAME, 'iframe')
        if frames:
            for frame in frames:
                if frame.get_attribute('name') == 'frmcenterandchat':
                    self.driver.switch_to.frame("frmcenterandchat")
                    self.driver.switch_to.frame("frmcentral")
                    break

    def try_to_switch_to_dialog(self):
        """Переключается на фрейм диалога."""
        frames = self.driver.find_elements(By.TAG_NAME, 'iframe')
        if frames:
            for frame in frames:
                if frame.get_attribute('id') == 'thedialog':
                    self.driver.switch_to.frame("thedialog")
                    break

    def try_to_click_to_glade_fairy(self):
        """Ищет фею поляны и щёлкает на неё."""
        glade_fairy = self.driver.find_elements(
                        By.CSS_SELECTOR,
                        'img[id="roomnpc231778"]')
        if not glade_fairy:
            glade_fairy = self.driver.find_elements(
                        By.CSS_SELECTOR,
                        'img[id="roomnpc17481"]')

        if len(glade_fairy) > 0:
            glade_fairy[0].click()
            sleep(1)

    def fight(self):
        """Проводит бой."""
        while self.driver.find_elements(
                        By.PARTIAL_LINK_TEXT, 'Ударить'):
            hits = self.driver.find_elements(
                By.CSS_SELECTOR,
                'img[onclick="touchFight();"]')
            if hits:
                hits[0].click()
            sleep(0.5)

    def send_photo(self, bot, photo):
        """Отправляет фотку в телеграм."""
        bot.send_photo(TELEGRAM_CHAT_ID, open(photo, 'rb'))

    def check_kaptcha(self, bot=None):
        """Проверяет наличие капчи на странице."""
        kaptcha = self.driver.find_elements(
                    By.CSS_SELECTOR,
                    'img[src="/inner/img/bc.php"]'
                )
        if kaptcha:
            print('Обнаружена капча!')
            kaptcha[0].screenshot('kaptcha.png')
            sleep(30)
            if bot is not None:
                self.send_photo(bot, 'kaptcha.png')
                sleep(1)
                self.send_photo(bot, 'runes.png')
                sleep(30)
        self.driver.refresh()

    def glade_farm(self, price_dict=FIELD_PRICES):
        """Фарм поляны(пока без распознования капчи)"""
        while True:
            sleep(1)
            try:
                self.try_to_switch_to_central_frame()
                self.try_to_click_to_glade_fairy()
                self.try_to_switch_to_dialog()
                glade_fairy_answers = self.driver.find_elements(
                    By.CLASS_NAME,
                    'talksayTak')
                if glade_fairy_answers:
                    if len(glade_fairy_answers) == 1:
                        wait_tag = self.driver.find_elements(
                            By.CLASS_NAME,
                            'talksayBIG')
                        if wait_tag:
                            sleep(time_extractor(wait_tag[0].text))
                        glade_fairy_answers[0].click()
                        continue
                    if len(glade_fairy_answers) == 3:
                        glade_fairy_answers[1].click()
                        sleep(1)
                    if len(glade_fairy_answers) > 3:
                        resurses = self.driver.find_elements(By.TAG_NAME, 'li')
                        if resurses:
                            res_price = [res.text for res in resurses]
                            print(res_price)
                            most_cheep_res = price_counter(
                                res_price,
                                price_diсt=price_dict)
                            now = datetime.now().strftime(TIME_FORMAT)
                            message_for_log = (
                                f'{res_price[most_cheep_res]} {now}')
                            print(message_for_log)
                            with open(
                                'glade_farm.txt',
                                "r+",
                                encoding="utf-8"
                            ) as file:
                                content = file.read()
                                file.seek(0)
                                file.write(f'{message_for_log}\n')
                                file.write(content)

                            glade_fairy_answers[most_cheep_res].click()
                self.fight()
                come_back = self.driver.find_elements(
                        By.PARTIAL_LINK_TEXT, 'Вернуться')
                if come_back:
                    come_back[0].click()
                    continue
                self.check_kaptcha()
            except Exception as e:
                print(e)
                sleep(2)
                if self.driver.session_id:
                    self.driver.refresh()
                    continue
                break


class HaddanBot:

    """Бот класс управления действиями персонажа.

    Принимает два обязательных аргумента при инициализации:
        char - никнейм персонажа,
        driver - объект класса webdriver.Chrome.

    """

    def __init__(self, char, driver, password, bot=None):
        self.driver = driver
        self.char = char
        self.password = password
        if bot is not None:
            self.bot = bot
        self.login_url = HADDAN_MAIN_URL

    def login_to_game(self):
        """Заходит в игру под заданным именем char."""
        self.driver.get(self.login_url)
        self.driver.maximize_window()
        sleep(1)
        username_field = self.driver.find_element(
            By.NAME, 'username')
        username_field.send_keys(self.char)
        sleep(1)
        password_field = self.driver.find_element(
            By.NAME, 'passwd')
        password_field.send_keys(self.password)
        sleep(1)
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR,
            '[href="javascript:enterHaddan()"]')
        submit_button.click()
        sleep(4)
