"""Сборщик цен ресурсов поляны"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


GLADE_PRICES = {
    'Мухожор': 9,
    'Подсолнух': 15,
    'Капустница': 27,
    'Мандрагора': 50,
    'Зеленая массивка': 68,
    'Колючник Черный': 101,
    'Гертаниум': 210
}


RES_LIST = ['Мухожор', 'Подсолнух', 'Капустница', 'Мандрагора',
            'Зеленая массивка', 'Колючник черный', 'Гертаниум']

SHOP_URL = 'http://ordenpegasa.ru/shop/'


def res_price_finder(driver, res):
    res_label = driver.find_elements(
        By.CSS_SELECTOR,
        f'input[value="{res}"]'
    )
    if res_label:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(res_label[0]))
        res_label[0].click()
    sleep(2)
    all_shops = driver.find_element(
        By.CSS_SELECTOR, 'table[id="response"]'
    )
    shops = all_shops.find_elements(
        By.TAG_NAME, 'tr'
    )
    first_shop_price = shops[1].text.split()
    if len(first_shop_price) == 4:
        return first_shop_price[2]
    return first_shop_price[3]


def get_glade_price_list(manager):
    manager.options.add_argument('--headless')
    manager.start_driver()
    manager.driver.get(SHOP_URL)
    glade_button = manager.driver.find_elements(
        By.CSS_SELECTOR,
        'label[for="tab_4"]'
    )
    if glade_button:
        glade_button[0].click()
    sleep(1)
    result = []
    for res in RES_LIST:
        result.append(
            res_price_finder(manager.driver, res)
        )
    for key, value in zip(GLADE_PRICES.keys(), result):
        GLADE_PRICES[key] = float(value)
    return GLADE_PRICES

