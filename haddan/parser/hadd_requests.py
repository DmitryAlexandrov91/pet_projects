from bs4 import BeautifulSoup
from requests_html import HTMLSession


URL = 'https://www.haddan.ru/thing.php?id=166819796'


if __name__ == '__main__':
    session = HTMLSession()
    response = session.get(URL)
    response.html.render(sleep=1)
    soup = BeautifulSoup(response.html.html, 'lxml')
    name = soup.find('td', {'class': 'description'}).h3.text
