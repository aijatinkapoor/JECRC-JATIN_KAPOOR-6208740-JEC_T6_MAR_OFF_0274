from selenium import webdriver
import time


url = "https://google.com"

for i in ['Chrome', 'Edge', 'Firefox']:

    if i == 'Chrome':
        driver = webdriver.Chrome()

    elif i == 'Edge':
        driver = webdriver.Edge()

    elif i == 'Firefox':
        driver = webdriver.Firefox()



    driver.get(url)

    print("URL:", url)
    print("Browser:", i)
    print("Title:", driver.title)

    time.sleep(3)
    driver.quit()