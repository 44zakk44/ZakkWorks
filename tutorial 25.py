import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 3
    while page <= max_pages:
        url = 'https://www.centrumrowerowe.pl/buty-rowerowe/szukanie,3,0,0,' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('img', {'class': 'level-0 image-layout resource-layout'}):
            src = link.get('src')
            print(src)
        page += 1

trade_spider(3)


# no i dupa..... sie zepuło xddd