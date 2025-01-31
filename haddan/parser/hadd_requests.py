from bs4 import BeautifulSoup
from requests_html import HTMLSession


URL = 'https://www.haddan.ru/thing.php?id=166819796'
THINGS_API_URL = 'https://haddan.ru/inner/api_lib.php?cat=thingtype&t=0'


def parse_libriary(page, session):
    

    


if __name__ == '__main__':
    session = HTMLSession()
    response = session.get(THINGS_API_URL)
    response.html.render(sleep=3)
    soup = BeautifulSoup(response.html.html, 'lxml')
    