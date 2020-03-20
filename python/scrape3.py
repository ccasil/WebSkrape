import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://www.w3schools.com/colors/colors_hex.asp')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

colors = soup.find('div', { 'id': 'colornamestable' })
# div = colors.find('div')
# print(div)

data = []
for d in colors.find_all('div'):
	for span in d.find_all('span', { 'class': 'colorhexspan' }):
		row = span.text
		print(row)