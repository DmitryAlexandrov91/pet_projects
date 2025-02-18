from telebot import TeleBot
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from constants import HADDAN_MAIN_URL, KAPCHA_PATH, TELEGRAM_BOT_TOKEN

from utils import send_photo, login_to_haddan, get_temple_kaptcha


bot = TeleBot(token=TELEGRAM_BOT_TOKEN)

# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


# @bot.message_handler(commands=['start'])
# def login_game(message):
#     chat = message.chat
#     chat_id = chat.id
    


@bot.message_handler(commands=['meditation'])
def minee(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(
        chat_id=chat_id,
        text='Заходим в игру и ищем капчу.'
    )

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # Открываем главную страницу игры.
    driver.get(HADDAN_MAIN_URL)
    driver.maximize_window()
    sleep(1)

    # Логинимся и ждём 5 секунд прогрузки страницы.
    login_to_haddan(driver)
    sleep(5)
    try:
        image_element = get_temple_kaptcha(driver)
        image_element.screenshot(f'{KAPCHA_PATH}')
        send_photo(bot, KAPCHA_PATH)
    except Exception:
        bot.send_message(
            chat_id=chat_id,
            text='Капча не обнаружена'
        )


@bot.message_handler(content_types=['text'])
def say_hi(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text='Привет, я копать!')


bot.polling()
