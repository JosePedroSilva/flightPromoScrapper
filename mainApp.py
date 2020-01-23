import requests
from bs4 import BeautifulSoup

kw = ['portugal', 'brasil', 'brazil', 'porto', 'oporto',
      'porto alegre', 'rio de janeiro', 'são paulo', 'canada', 'lisbon', 'lisboa']

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


def fly4free(kw, headers):
    """
        Search for promos on www.fly4free.com
    """
    URL_fly4free = 'https://www.fly4free.com/flights/flight-deals/europe/'

    page_fly4free = requests.get(URL_fly4free, headers=headers)
    soup_fly4free = BeautifulSoup(page_fly4free.text, 'html.parser')
    result_fly4free = str(soup_fly4free.findAll(attrs='entry__title'))
    for word in kw:
        if word.lower() in result_fly4free.lower():
            print(f'Found {word} in fly4free')


def travelfree(kw, headers):
    URL_travelfree = 'https://travelfree.info/'

    page_travelfree = requests.get(URL_travelfree, headers=headers)
    soup_travelfree = BeautifulSoup(page_travelfree.text, 'html.parser')
    result_travelfree = str(soup_travelfree.findAll(
        attrs='post-title entry-title'))
    for word in kw:
        if word.lower() in result_travelfree.lower():
            print(f'Found {word} in travelfree')


fly4free(kw, headers)
travelfree(kw, headers)
