from bs4 import BeautifulSoup
import requests
from csv import writer
url = "https://www.pararius.com/apartments/den-haag"
page = requests.get(url)
print(page)
print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('selection',class_="listing-search-item")
print(lists)
for list in lists:
    title = lists.find('a',class_="listing-search-item__link--title").text.replace('\n', '')
    price = lists.find('a',class_="listing-search-item__price").text.replace('\n', '')
    location = list.find('div', class_="listing-search-item__location").text.replace('\n', '')
    area = list.find('span', class_="illustrated-features__description").text.replace('\n', '')
    info = [title, price, location,  area]
    print(info)
