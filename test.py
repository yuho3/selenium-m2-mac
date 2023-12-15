from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import os
import time

url = "https://google.com"
keyword = "スクレイピング"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor = 'http://selenium:4444/wd/hub',
    options = webdriver.ChromeOptions()
)

driver.get(url)
driver.find_element(By.NAME, "q").send_keys(keyword + Keys.RETURN)

driver.quit()
