import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# играемся с элементами navigation bar
nav = soup.nav


for url in nav.find_all('a'):
    print(url.get('href'))

# играемся с элементами body
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

for div in soup.find_all('div', class_='body'):
    print(div.text)

