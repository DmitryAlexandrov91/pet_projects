from time import sleep

from haddan.haddan_miner.tel_bot import save_url_content, send_photo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from constants import HADDAN_MAIN_URL, KAPCHA_PATH, PASSWORD, USERNAME

if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Открываем главную страницу игры.
    driver.get(HADDAN_MAIN_URL)
    driver.maximize_window()
    sleep(1)

    # Логинимся и ждём 5 секунд прогрузки страницы.
    username_field = driver.find_element(By.NAME, 'username')
    username_field.send_keys(USERNAME)
    sleep(1)
    password_field = driver.find_element(By.NAME, 'passwd')
    password_field.send_keys(PASSWORD)
    sleep(1)
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        '[href="javascript:enterHaddan()"]')
    submit_button.click()
    sleep(5)

    # Переключаемся в комнату копки/медатации.
    driver.switch_to.frame("frmcenterandchat")
    driver.switch_to.frame("frmcentral")

    # Нажимаем кнопку медитация.
    meditation_link = driver.find_element(By.LINK_TEXT, "медитация")
    meditation_link.click()
    sleep(3)

    # Переключаемся на фрейм с медитацией
    driver.switch_to.frame("func")

    # Находим экапчу и отправляем в телеграм
    image_element = driver.find_element(
        By.CSS_SELECTOR,
        'img[src="/inner/img/gc.php"]')
    image_element.screenshot(f'{KAPCHA_PATH}')
    send_photo(KAPCHA_PATH)

    # meditation_button = driver.find_element(By.CLASS_NAME, "bright")
    # meditation_button.click()

    # driver.execute_script("window.open('');")
    # driver.switch_to.window(driver.window_handles[-1])
    # driver.get(MEDITATION_URL)
    # sleep(3)

    # driver.switch_to.frame("func")

    # kapcha_element = driver.find_element(By.XPATH, "//img[@src='/inner/img/gc.php']")
    # kapcha_url = kapcha_element.get_attribute("src")

    # driver.execute_script("window.open('');")
    # driver.switch_to.window(driver.window_handles[-1])
    # driver.get(kapcha_url)
    # sleep(500)
    


    # page_source = driver.page_source
    # with open("page_source.html", "w", encoding="utf-8") as file:
    #     file.write(page_source)


    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "bright"))
    # )
    # print(element.text)
    # element.click()
    # sleep(3)


    
    # driver.save_screenshot('temp/meditation.png')

    # bot.send_photo(TELEGRAM_CHAT_ID, 'temp/meditation.png')


    
    


    # meditation_button = driver.find_element(By.CSS_SELECTOR, 'a.bright[href*="temple"]')
    # meditation_button.click()
    # sleep(999)

    # # Сохранение скриншота страницы с заданным именем.
    # driver.save_screenshot('screenshot.png')
    # sleep(PAUSE_DURATION_SECONDS)

    # # Поиск первого поста на странице по классу.
    # first_post = driver.find_element(By.CLASS_NAME, 'card-text')
    # # Вывод текста найденного элемента в терминал.
    # print(first_post.text)
    # Закрытие веб-драйвера.


# # Ваш токен бота Telegram
# TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
# # Ваш chat_id в Telegram
# CHAT_ID = 'YOUR_CHAT_ID'

# def extract_image_url(url):
#     # Получаем содержимое страницы
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Находим все теги img
#         images = soup.find_all('img')
        
#         if images:
#             return images[0].get('src')  # Возвращаем URL первой найденной картинки
#     else:
#         print(f"Ошибка получения страницы: {response.status_code}")

# def send_image_to_telegram(image_url):
#     bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
#     try:
#         # Скачиваем изображение
#         image_data = requests.get(image_url).content
        
#         # Отправляем изображение в Telegram
#         bot.send_photo(chat_id=CHAT_ID, photo=image_data)
#         print("Изображение успешно отправлено!")
#     except Exception as e:
#         print(f"Произошла ошибка при отправке изображения: {e}")

# if __name__ == "__main__":
#     # Пример URL сайта, где нужно найти изображение
#     website_url = 'https://example.com/'
    
#     # Извлекаем URL изображения
#     image_url = extract_image_url(website_url)
    
#     if image_url:
#         send_image_to_telegram(image_url)
#     else:
#         print("Не удалось найти изображение.")
