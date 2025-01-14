import requests
import requests_cache

from bs4 import BeautifulSoup


PEGAS_CLAN_URL = 'https://haddan.ru/clan/clan.php?id=pegas'
MY_URL = 'https://haddan.ru/user.php?id=480907'


# Запрос через кешированную сессию
session = requests_cache.CachedSession()

response = session.get(PEGAS_CLAN_URL)
my_info = session.get(MY_URL)
clan_info = BeautifulSoup(response.text, 'lxml')
my_info = BeautifulSoup(my_info.text, 'lxml')

