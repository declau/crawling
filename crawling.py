from bs4 import BeautifulSoup

import requests

URL = 'https://pt.wikipedia.org/'

headers = headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}


def find_links():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = []
    for l in soup.find_all('a', href=True):
        links.append(l['href'])
    return links


print(find_links())
