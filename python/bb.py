import requests
from bs4 import BeautifulSoup

MAINSTR = ''

exercisedatabasepages = []

databasepage = 'https://www.bodybuilding.com/exercises'
databasedata = requests.get(databasepage)
soup = BeautifulSoup(databasedata.text, 'html.parser')
leftside = soup.find('ul', {'class': 'exercise-list-left'})
leftlinks = leftside.find_all('a')
for item in leftlinks:
    exercisedatabasepages.append('https://www.bodybuilding.com' + item['href'])

# print(exercisedatabasepages)

pages = []

for url in exercisedatabasepages: 
    maindata = requests.get(url)
    soup = BeautifulSoup(maindata.text, 'html.parser')
    links = soup.find_all('a', {'itemprop': 'name'})
    for item in links:
        pages.append('https://www.bodybuilding.com' + item['href'])

    print(pages)


for url in pages:
    # get the data
    data = requests.get(url)

    # load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    vid = soup.find('img', {'class': 'bb-gated-video--stockThumb'})
    vidtxt = vid['src'].split('/')
    title = soup.find('h1', {'itemprop': 'name'})
    if 'media' in vidtxt:
        index = vidtxt.index('media')
    elif 'images' in vidtxt:
        index = vidtxt.index('images')
    # print(div)
    print(title.text.strip())
    print ('https://content.jwplatform.com/videos/' + vidtxt[index + 1] + '-1zuboWt3.mp4')

    MAINSTR += title.text.strip() + ',' + 'https://content.jwplatform.com/videos/' + vidtxt[index + 1] + '-1zuboWt3.mp4,'
