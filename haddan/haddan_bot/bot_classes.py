"""Классые управления работой бота.

DriverManager - класс управления объектом webdriver
HaddanBot  - класс управления действиями персонажа.
"""
import threading
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from constants import HADDAN_MAIN_URL


class DriverManager:

    """Класс управления объектом driver."""

    def __init__(self, options=None):
        self.driver = None
        self.thread = None
        self.options = webdriver.ChromeOptions()

    def start_driver(self):
        if self.driver is None or self.driver.session_id is None:
            service = Service(executable_path=ChromeDriverManager().install())
            self.driver = webdriver.Chrome(
                service=service,
                options=self.options)
            self.thread = threading.current_thread()

    def close_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
            self.thread = None

    def get_active_driver(self):
        return self.driver

    def save_url_content(self):
        """Сохраняет контент страницы."""
        page_source = self.driver.page_source
        with open('page.html]', "w", encoding="utf-8") as file:
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


class HaddanBot():

    """Бот класс управления действиями персонажа.

    Принимает два обязательных аргумента при инициализации:
        char - никнейм персонажа,
        driver - обхект класса webdriver.Chrome.

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
