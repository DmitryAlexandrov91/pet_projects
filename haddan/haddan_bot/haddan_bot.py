"""Бот хаддан без TG."""
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from constants import FIRST_CHAR, SECOND_CHAR, PASSWORD, FIELD_PRICES, TIME_FORMAT
from utils import (HaddanBot, price_counter, send_photo, time_extractor,
                   try_to_switch_to_central_frame, try_to_switch_to_dialog,
                   fight, check_kaptcha, try_to_click_to_glade_fairy,
                   select_slot, select_spell)


def kaptcha_find(driver, bot=None):
    try_to_switch_to_central_frame(driver)
    kaptcha = driver.find_elements(
                By.CSS_SELECTOR,
                'img[src="/inner/img/bc.php"]'
            )
    if kaptcha:
        print('Обнаружена капча!')
        kaptcha[0].screenshot('kaptcha.png')
        send_photo(bot, 'kaptcha.png')
        sleep(1)
        send_photo(bot, 'runes.png')
        sleep(60)


def glade_farm(driver, price_dict=FIELD_PRICES, bot=None):
    """Фарм поляны(пока без распознования капчи)"""
    while True:
        try:
            try_to_switch_to_central_frame(driver)
            try_to_click_to_glade_fairy(driver)
            try_to_switch_to_dialog(driver)
            glade_fairy_answers = driver.find_elements(
                By.CLASS_NAME,
                'talksayTak')
            if glade_fairy_answers:
                if len(glade_fairy_answers) == 1:
                    wait_tag = driver.find_elements(
                        By.CLASS_NAME,
                        'talksayBIG')
                    if wait_tag:
                        sleep(time_extractor(wait_tag[0].text))
                        glade_fairy_answers[0].click()
                    continue
                if len(glade_fairy_answers) > 1 and len(glade_fairy_answers) < 5:
                    glade_fairy_answers[1].click()
                    sleep(1)
                if len(glade_fairy_answers) > 4:
                    resurses = driver.find_elements(By.TAG_NAME, 'li')
                    if resurses:
                        res_price = [res.text for res in resurses]
                        most_cheep_res = price_counter(
                            res_price,
                            price_diсt=price_dict)
                        now = datetime.now().strftime(TIME_FORMAT)
                        message_for_log = f'{res_price[most_cheep_res]} {now}'
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
            fight(driver)
            come_back = driver.find_elements(
                    By.PARTIAL_LINK_TEXT, 'Вернуться')
            if come_back:
                come_back[0].click()
                continue
            check_kaptcha(driver, bot=bot)
        except Exception as e:
            print(e)
            sleep(2)
            if driver.session_id:
                driver.refresh()
                continue
            break


def lab_spirits_play(driver):
    """Скрипт бега по лабиринту и фарма мобов."""


if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    SwordS = HaddanBot(char=FIRST_CHAR, driver=driver)
    SwordS.login_to_game(PASSWORD)

    # Nordman = HaddanBot(char=SECOND_CHAR, driver=driver)
    # Nordman.login_to_game(PASSWORD)

    glade_farm(driver)
