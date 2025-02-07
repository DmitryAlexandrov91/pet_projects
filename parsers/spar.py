from bs4 import BeautifulSoup
from requests_html import HTMLSession


SPAR_CATALOG = 'https://myspar.ru/catalog/'

TIMEOUT = 1


if __name__ == '__main__':
    session = HTMLSession()
    response = session.get(SPAR_CATALOG)
    response.html.render(sleep=TIMEOUT)
    soup = BeautifulSoup(response.html.html, 'lxml')
    print(soup.prettify())
