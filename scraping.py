import bs4 as bs
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

"""
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
"""


#table = soup.table
table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

# поулчить таблицы с сайта при помощи pandas
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
for df in dfs:
    print(df)


# работа с xml
sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(sauce, 'xml')

for url in soup.find_all('loc'):
    print(url.text)