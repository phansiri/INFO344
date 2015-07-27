__author__ = 'Phansiri'


import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://students.washington.edu/phansiri/'\
              # + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
