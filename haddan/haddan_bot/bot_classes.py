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


class HaddanBot():

    """Бот класс управления действиями персонажа.

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
