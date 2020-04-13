"""Runs the webscrapper and prints the results on the console.

Requires:
-os
-pyfiglet
"""
import os
from webScrapper import *
from pyfiglet import figlet_format

kw = ['portugal', 'brasil', 'brazil', 'porto', 'oporto',
      'porto alegre', 'rio de janeiro', 'são paulo', 'canada', 'lisbon', 'lisboa']

Agent = os.environ.get('WebAgent')
headers = {
    "User-Agent": Agent}


if __name__ == '__main__':
    print(figlet_format("Promo Scanner"))
    print('Flight4Free:')
    fly4free(kw, headers)
    print('')
    print('TravelFree:')
    travelfree(kw, headers)
    print('')
