from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(3)

'''gender = driver.find_elements(By.XPATH, '//input[@name = "gender"]')
for g in gender:
    g.click()
    sleep(2)'''


days = driver.find_elements(By.XPATH, '//div/div/input[@type="checkbox"]')
for day in days:
    day.click()
    print(day.get_attribute('value'))

days = days[::-1]
for day in days:
    day.click()

driver.quit()
