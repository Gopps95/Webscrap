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
driver.get("https://www.robinsharma.com/")
driver.maximize_window()

links = driver.find_elements("xpath","//a[@href]")

book_picture = driver.find_element(By.XPATH,'//img[@alt="Robin Sharma"]')
book_picture.click()

try:
    wait = WebDriverWait(driver, 10)
    new_window = wait.until(EC.new_window_is_opened)
    driver.switch_to.window(new_window)
except WebDriverException as e:
    print(f"Error switching to new window: {e}")

