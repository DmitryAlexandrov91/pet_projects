"""Бот хаддан без TG."""
from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from constants import FIRST_CHAR, GLADE_FARM_LOG_PATH, SECOND_CHAR
from utils import (HaddanBot, price_counter, time_extractor,
                   try_to_switch_to_central_frame, try_to_switch_to_dialog)


def glade_farm(driver):
    """Фарм поляны(пока без распознования капчи)"""
    while True:
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
                try:
                    battle_start[0].click()
                except Exception:
                    driver.refresh()
                    continue
                continue
            if len(battle_start) > 1 and len(battle_start) < 5:
                battle_start[1].click()
                sleep(1)
            if len(battle_start) > 4:
                resurses = driver.find_elements(By.TAG_NAME, 'li')
                if resurses:
                    res_price = [res.text for res in resurses]
                    most_cheep_res = price_counter(res_price)
                    message_for_log = f'Выбрано: {res_price[most_cheep_res]} - {datetime.now().time()}'
                    print(message_for_log)
                    with open(GLADE_FARM_LOG_PATH, "a", encoding="utf-8") as file:
                        file.write(message_for_log)
                    battle_start[most_cheep_res].click()
        while driver.find_elements(
                By.PARTIAL_LINK_TEXT, 'Ударить'):
            hit = driver.find_element(
                By.CSS_SELECTOR,
                'img[onclick="touchFight();"]')
            hit.click()
            sleep(0.5)
        come_back = driver.find_elements(
                By.PARTIAL_LINK_TEXT, 'Вернуться')
        if come_back:
            come_back[0].click()
        else:
            sleep(1)
            driver.refresh()
            continue


if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    SwordS = HaddanBot(char=FIRST_CHAR, driver=driver)
    SwordS.login_to_game()

    glade_farm(driver)
