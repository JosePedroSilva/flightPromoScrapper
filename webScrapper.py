"""Webscrapping of fly4free and travelfree 

Arguments:
-Keywords to search
-headers

Requires:
-requests
-bs4
"""
import requests
from bs4 import BeautifulSoup

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
            print(f'Found {word}')


def travelfree(kw, headers):
    """
        Search for promos on www.travelfree.info/
    """
    URL_travelfree = 'https://www.travelfree.info/'

    page_travelfree = requests.get(URL_travelfree, headers=headers)
    soup_travelfree = BeautifulSoup(page_travelfree.text, 'html.parser')
    result_travelfree = str(soup_travelfree.findAll(
        attrs='post-title entry-title'))
    for word in kw:
        if word.lower() in result_travelfree.lower():
            print(f'Found {word}')



