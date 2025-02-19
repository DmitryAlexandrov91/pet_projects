from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from telebot import TeleBot, types
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

from constants import (FIRST_CHAR, SCREENSHOT_PATH, SECOND_CHAR,
                       TELEGRAM_BOT_TOKEN)
from utils import (HaddanBot, save_url_content, send_photo,
                   switch_to_central_frame)

bot = TeleBot(token=TELEGRAM_BOT_TOKEN)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_html = types.KeyboardButton('/html')
button_location = types.KeyboardButton('/location')
button_field_farm = types.KeyboardButton('/field_farm')
keyboard.add(button_html)
keyboard.add(button_location)
keyboard.add(button_field_farm)

SwordS = HaddanBot(char=FIRST_CHAR, bot=bot, driver=driver)
Nordman = HaddanBot(char=SECOND_CHAR, bot=bot, driver=driver)



@bot.message_handler(commands=['1'])
def first_char_login_game(message):
    chat = message.chat
    chat_id = chat.id

    bot.send_message(
        chat_id=chat_id,
        text='Заходим в игру под главным персонажем.',
        reply_markup=keyboard,
    )
    SwordS.login_to_game()


@bot.message_handler(commands=['2'])
def second_char_login_game(message):
    chat = message.chat
    chat_id = chat.id

    bot.send_message(
        chat_id=chat_id,
        text='Заходим в игру под инкой.',
        reply_markup=keyboard,
    )
    Nordman.login_to_game()


@bot.message_handler(commands=['html'])
def get_page_html(message):
    chat = message.chat
    chat_id = chat.id
    save_url_content(driver)
    bot.send_message(
            chat_id=chat_id,
            text='html код страницы сохранён',
            reply_markup=keyboard,
        )


@bot.message_handler(commands=['location'])
def get_page_screenshot(message):
    chat = message.chat
    chat_id = chat.id
    switch_to_central_frame(driver)
    location = driver.find_element(
        By.CSS_SELECTOR,
        'img[name="mainimg"]')
    location.screenshot(f'{SCREENSHOT_PATH}')
    bot.send_message(
            chat_id=chat_id,
            text='Ваше местоположение.',
            reply_markup=keyboard,
        )
    send_photo(bot, SCREENSHOT_PATH)


@bot.message_handler(commands=['field_farm'])
def field_farm(message):
    chat = message.chat
    chat_id = chat.id
    frames = driver.find_elements(By.TAG_NAME, 'iframe')
    if frames:
        for frame in frames:
            print(frame.name)
                

# @bot.message_handler(commands=['work'])
# def mine(message):
#     chat = message.chat
#     chat_id = chat.id
#     try:
#         image_element = get_mine_kaptcha(driver)
#         image_element.screenshot(f'{KAPCHA_PATH}')
#         send_photo(bot, KAPCHA_PATH)
#     except Exception:
#         image_element = find_kaptcha(driver)
#         image_element.screenshot(f'{KAPCHA_PATH}')
#         send_photo(bot, KAPCHA_PATH)
#     except Exception:
#         save_url_content(driver)
#         bot.send_message(
#             chat_id=chat_id,
#             text='Не удалось найти капчу, сохранил страницу для анализа.',
#             reply_markup=keyboard,
#         )


# @bot.message_handler(commands=['html'])
# def get_page_html(message):
#     save_url_content(driver)
#     chat = message.chat
#     chat_id = chat.id
#     bot.send_message(
#             chat_id=chat_id,
#             text='html код страницы сохранён',
#             reply_markup=keyboard,
#         )


# @bot.message_handler(commands=['switch'])
# def switch_to_central(message):
#     chat = message.chat
#     chat_id = chat.id
#     try:
#         switch_to_central_frame(driver)
#     except Exception:
#         bot.send_message(
#             chat_id=chat_id,
#             text='Центральное окно не побнаружено.',
#             reply_markup=keyboard,
#         )


# @bot.message_handler(commands=['поляна'])
# def bot_farm_field(message):
#     farm_field(bot, driver, keyboard)


# @bot.message_handler(content_types=['text'])
# def kaptcha_handler(message):
#     chat = message.chat
#     chat_id = chat.id
#     text = message.text
#     try:
#         get_kaptcha_answer(text, driver)
#         bot.send_message(
#             chat_id=chat_id,
#             text='Правильный ответ, работа началась!',
#             reply_markup=keyboard,
#         )
#     except Exception:
#         bot.send_message(
#             chat_id=chat_id,
#             text='Не удалось ввести капчу!',
#             reply_markup=keyboard,
#         )


def main():
    bot.polling()


if __name__ == '__main__':
    main()
