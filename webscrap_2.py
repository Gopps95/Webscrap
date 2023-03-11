from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

 
options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.robinsharma.com/")
driver.maximize_window()


links = driver.find_elements("xpath","//a[@href]")

for link in links:
    if "style_books_col__3U9Vo" in link.get_attribute("innerHTML"):
        link.click()
        break


book_links = driver.find_elements("xpath",
                                  "//div[contains(@class,'style_books_col__3U9Vo')][count(.//a)=1]//a")

for book_link in book_links:
    print(book_link.get_attribute("innerHTML"))