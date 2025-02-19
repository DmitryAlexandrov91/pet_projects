"""Код логики работы, основанный на классе."""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from constants import SECOND_CHAR, FIELD_PRICES
from utils import HaddanBot, save_url_content, price_counter


if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    Nordman = HaddanBot(char=SECOND_CHAR, driver=driver)
    Nordman.login_to_game()

    while True:
        frames = driver.find_elements(By.TAG_NAME, 'iframe')
        if frames:
            for frame in frames:
                if frame.get_attribute('name') == 'frmcenterandchat':
                    driver.switch_to.frame("frmcenterandchat")
                    driver.switch_to.frame("frmcentral")
                    break
        glade_fairy = driver.find_elements(
                By.CSS_SELECTOR,
                'img[id="roomnpc231778"]')
        if len(glade_fairy) > 0:
            glade_fairy[0].click()
            sleep(5)
        frames = driver.find_elements(By.TAG_NAME, 'iframe')
        if frames:
            for frame in frames:
                if frame.get_attribute('id') == 'thedialog':
                    driver.switch_to.frame("thedialog")
        battle_start = driver.find_elements(
            By.CLASS_NAME,
            'talksayTak')
        if battle_start:
            if len(battle_start) == 1:
                battle_start[0].click()
                sleep(30)
                continue
            if len(battle_start) > 1 and len(battle_start) < 5:
                battle_start[1].click()
                sleep(5)
            if len(battle_start) > 4:
                resurses = driver.find_elements(By.TAG_NAME, 'li')
                if resurses:
                    res_price = [res.text for res in resurses]
                    most_cheep_res = price_counter(res_price)
                    battle_start[most_cheep_res].click()
            else:
                wait_tag = driver.find_elements(
                    By.CLASS_NAME,
                    'talksayBIG')
                if wait_tag:
                    if '0:00' in wait_tag[0].text:
                        driver.refresh()
                        continue
                    else:
                        sleep(30)
                        driver.refresh()
                        continue
        while driver.find_elements(
                By.PARTIAL_LINK_TEXT, 'Ударить'):
            hit = driver.find_element(
                By.CSS_SELECTOR,
                'img[onclick="touchFight();"]')
            hit.click()
            sleep(1)
        come_back = driver.find_elements(
                By.PARTIAL_LINK_TEXT, 'Вернуться')
        if come_back:
            come_back[0].click()
        else:
            driver.refresh()
            continue
