from bs4 import BeautifulSoup
import requests
from csv import writer
url = "https://www.pararius.com/apartments/den-haag"
page = requests.get(url)
print(page)
print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('selection',class_="listing-search-item")
