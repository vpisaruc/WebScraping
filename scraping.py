import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# поиск всех тегов p
#print(soup.find_all('p'))

# поиск дочерних элементов в родительском
# for paragraph in soup.find_all('p'):
#      print(paragraph.text)

# выдает весь текст на странице
# print(soup.get_text())

for url in soup.find_all('a'):
    print(url.get('href'))