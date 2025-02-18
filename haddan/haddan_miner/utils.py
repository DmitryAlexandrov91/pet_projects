"""Утилитки приложения haddan_miner"""
from time import sleep
from constants import PAGE_SOURCE_PATH, PASSWORD, TELEGRAM_CHAT_ID, USERNAME
from selenium.webdriver.common.by import By


def send_photo(bot, photo):
    """Отправляет фотку в телеграм."""
    bot.send_photo(TELEGRAM_CHAT_ID, open(photo, 'rb'))


def save_url_content(driver):
    """Сохраняет контент страницы."""
    page_source = driver.page_source
    with open(PAGE_SOURCE_PATH, "w", encoding="utf-8") as file:
        file.write(page_source)


def login_to_haddan(driver):
    """Вход в игру."""
    username_field = driver.find_element(
        By.NAME, 'username')
    username_field.send_keys(USERNAME)
    sleep(1)
    password_field = driver.find_element(
        By.NAME, 'passwd')
    password_field.send_keys(PASSWORD)
    sleep(1)
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        '[href="javascript:enterHaddan()"]')
    submit_button.click()


def get_temple_kaptcha(driver):
    """Возвращает картинку  капчей из храма."""
    # Переключаемся в комнату медатации.
    driver.switch_to.frame("frmcenterandchat")
    driver.switch_to.frame("frmcentral")
    # Нажимаем кнопку медитация.
    meditation_link = driver.find_element(By.LINK_TEXT, "медитация")
    meditation_link.click()
    sleep(1)
    # Переключаемся на фрейм с медитацией
    driver.switch_to.frame("func")
    # Находим экапчу и отправляем в телеграм
    image_element = driver.find_element(
        By.CSS_SELECTOR,
        'img[src="/inner/img/gc.php"]')
    return image_element
