import requests
from bs4 import BeautifulSoup

pages = ['https://www.apple.com/shop/iphone/iphone-accessories/power-cables', 'https://www.apple.com/shop/iphone/iphone-accessories/power-cables?page=2']

url = ''
for item in pages:
    url = item
    # get the data
    data = requests.get(url)

    # load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    products = soup.find('div', { 'class': 'column small-12 as-search-results-tiles as-search-results-width' })
    div = products.find('div', { 'class': 'as-producttile large-4 small-6' })

    data = []
    finisheddata = []
    for d in products.find_all('div', { 'class': 'as-producttile-titlepricewraper'}):
        for title in d.find_all('span'):
            data.append(title.text)
        for price in d.find_all('div', { 'class': 'as-price-currentprice as-producttile-currentprice'}):
            data.append(price.text)
        for item in data:
            item = item.replace('\n', '').replace('\t', '')
            # finisheddata.append(item)
            print(item)
    # print(data)
