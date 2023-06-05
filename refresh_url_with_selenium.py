
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://mail.google.com/mail/u/0/zzzzzz"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)

time.sleep(5)
driver.refresh()