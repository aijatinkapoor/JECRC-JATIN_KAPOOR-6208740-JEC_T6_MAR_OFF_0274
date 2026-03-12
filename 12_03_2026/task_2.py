from selenium import webdriver
import time

for i in ['Chrome', 'Edge', 'Firefox']:

    if i == 'Chrome':
        driver = webdriver.Chrome()

    elif i == 'Edge':
        driver = webdriver.Edge()

    elif i == 'Firefox':
        driver = webdriver.Firefox()

    driver.get("https://www.google.com")
    time.sleep(3)
    driver.quit()