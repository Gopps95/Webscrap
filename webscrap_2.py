from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.neuralnine.com/")
driver.maximize_window()

links = driver.find_elements("xpath","//a[@href]")

for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break
book_links = driver.find_elements("xpath","//div[contains(@class,'elementor-column-wrap')][.//h2[text()[contains(.,'7 IN 1')]]][count(.//a)=2]//a")

book_links[0].click()

driver.switch_to.window(driver.window_handles[1])