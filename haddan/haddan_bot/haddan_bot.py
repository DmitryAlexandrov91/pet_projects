"""Бот хаддан без TG."""
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from constants import FIRST_CHAR, PASSWORD, TELEGRAM_CHAT_ID
from utils import (HaddanBot, price_counter, send_photo, time_extractor,
                   try_to_switch_to_central_frame, try_to_switch_to_dialog)


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


def glade_farm(driver, bot=None):
    """Фарм поляны(пока без распознования капчи)"""
    while True:
        try:
            try_to_switch_to_central_frame(driver)
            glade_fairy = driver.find_elements(
                    By.CSS_SELECTOR,
                    'img[id="roomnpc231778"]')
            if len(glade_fairy) > 0:
                glade_fairy[0].click()
                sleep(1)
            try_to_switch_to_dialog(driver)
            battle_start = driver.find_elements(
                By.CLASS_NAME,
                'talksayTak')
            if battle_start:
                if len(battle_start) == 1:
                    wait_tag = driver.find_elements(
                        By.CLASS_NAME,
                        'talksayBIG')
                    if wait_tag:
                        sleep(time_extractor(wait_tag[0].text))
                        battle_start[0].click()
                    continue
                if len(battle_start) > 1 and len(battle_start) < 5:
                    battle_start[1].click()
                    sleep(1)
                if len(battle_start) > 4:
                    resurses = driver.find_elements(By.TAG_NAME, 'li')
                    if resurses:
                        res_price = [res.text for res in resurses]
                        most_cheep_res = price_counter(res_price)
                        message_for_log = f'Выбрано: {res_price[most_cheep_res]} - {datetime.now()}'
                        print(message_for_log)
                        with open(
                            'glade_farm.txt',
                            "a",
                            encoding="utf-8"
                        ) as file:
                            file.write(f'{message_for_log}\n')
                        battle_start[most_cheep_res].click()
            while driver.find_elements(
                    By.PARTIAL_LINK_TEXT, 'Ударить'):
                hits = driver.find_elements(
                    By.CSS_SELECTOR,
                    'img[onclick="touchFight();"]')
                if hits:
                    hits[0].click()
                sleep(0.5)
            come_back = driver.find_elements(
                    By.PARTIAL_LINK_TEXT, 'Вернуться')
            if come_back:
                come_back[0].click()
                continue
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
        except Exception:
            sleep(2)
            driver.refresh()
            continue


if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    SwordS = HaddanBot(char=FIRST_CHAR, driver=driver)
    SwordS.login_to_game(PASSWORD)

    glade_farm(driver)
