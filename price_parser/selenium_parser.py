from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

from constants import OZON_MAIN_URL, CHROME_DRIVER_PATH


# Инициализация сервиса для драйвера
chrome_service = Service(CHROME_DRIVER_PATH)

# Инициализация веб-драйвера
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(service=chrome_service, options=options)

# Переход на нужную страницу
browser.get(OZON_MAIN_URL)

# Проверка существования элемента
page_source = browser.page_source

soup = BeautifulSoup(page_source, 'lxml')
print(soup)

# Закрыть браузер
browser.quit()
