from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from utils import price_formatter, list_combiner

# Если у вас установлен другой браузер - импортируйте нужный драйвер.
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.opera import OperaDriverManager

DJANGO_URL = 'https://myspar.ru/'
USERNAME = 'test_parser_user'
PASSWORD = 'testpassword'
PAUSE_DURATION_SECONDS = 5

if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(DJANGO_URL)
    driver.maximize_window()
    sleep(PAUSE_DURATION_SECONDS)

    # Поиск в содержимом страницы поля для логина.
    # Возможные варианты для поиска:
    # ID, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT,
    # NAME, TAG_NAME, CLASS_NAME, CSS_SELECTOR
    # username_input = driver.find_element(By.CLASS_NAME, 'header-main__catalog')

    # Щелчок и ввод текста в строку поиска.

    search_element = driver.find_element(
         By.CLASS_NAME, 'header-control__text-main')
    search_element.click()
    sleep(PAUSE_DURATION_SECONDS)
    text_field = driver.find_element(
        by="id", value="input-smartsearch")
    product_for_search = input("Введите продукт для поиска: ")
    text_field.send_keys(f"{product_for_search}")
    sleep(PAUSE_DURATION_SECONDS)




    # Щелчок по каталоку продуктов.
    # element = driver.find_element(
    #     By.CLASS_NAME, 'header-main__catalog')
    # element.click()
    # sleep(PAUSE_DURATION_SECONDS)

    # Выводит список всех категорий каталога.
    # categories = driver.find_elements(
    #    By.CSS_SELECTOR, '.menu-catalog__text')
    # categories_list = [category.text for category in categories]
    # print(set(categories_list))

    # Парсинг всех продуктов и их цен в определённой категории.
    # meet_bird = driver.find_element(
    #     By.PARTIAL_LINK_TEXT, 'Хлеб')
    # meet_bird.click()
    # sleep(PAUSE_DURATION_SECONDS)
    # pink = driver.find_element(
    #     By.PARTIAL_LINK_TEXT, 'Хлеб')
    # pink.click()
    # sleep(PAUSE_DURATION_SECONDS)
    # product_elements = driver.find_elements(
    #     By.CSS_SELECTOR, ".catalog-tile__name")
    # products = [price.text for price in product_elements]
    # price_elements = driver.find_elements(By.CSS_SELECTOR, ".prices__actual")
    # prices = [price_formatter(price.text) for price in price_elements]
    # results = list_combiner(products, prices)
    # print(results)

    # Ввод логина при помощи имитации ввода с клавиатуры.
    # username_input.send_keys(USERNAME)
    # sleep(PAUSE_DURATION_SECONDS)
    # Поиска поля для пароля.
    # password_input = driver.find_element(By.NAME, 'password')
    # # Ввод пароля.
    # password_input.send_keys(PASSWORD)
    # sleep(PAUSE_DURATION_SECONDS)

    # # Поиск кнопки "Войти".
    # submit_button = driver.find_element(By.TAG_NAME, 'button')
    # # Эмуляция щелчка мышью.
    # submit_button.click()
    # sleep(PAUSE_DURATION_SECONDS)

    # # Сохранение скриншота страницы с заданным именем.
    # driver.save_screenshot('screenshot.png')
    # sleep(PAUSE_DURATION_SECONDS)

    # # Поиск первого поста на странице по классу.
    # first_post = driver.find_element(By.CLASS_NAME, 'card-text')
    # # Вывод текста найденного элемента в терминал.
    # print(first_post.text)
    # Закрытие веб-драйвера.
    driver.quit()
