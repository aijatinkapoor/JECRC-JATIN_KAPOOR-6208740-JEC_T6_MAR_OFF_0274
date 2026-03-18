'''from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

name = driver.find_element(By.ID, 'name')
Email = driver.find_element(By.XPATH, '//input[@placeholder = "Enter EMail"]')

name.send_keys("Nikhil")
sleep(2)
# name.clear()
# sleep(2)
Email.send_keys("Nikhil@1234")
sleep(2)

# print(name.get_attribute('id'))
print(name.get_attribute('value'))
driver.quit()'''

''''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
driver.maximize_window()

sleep(5)

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("Shoes", Keys.ENTER)
# s_button = driver.find_element(By.ID, "nav-search-submit-button")
# s_button.click()
sleep(2)

# print(search.get_attribute('value'))

driver.quit()'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://www.bewakoof.com/")
driver.maximize_window()

sleep(5)

search = driver.find_element(By.XPATH, '//*[@id="__next"]/main/main/header/div/div[2]/div[2]/ul/li[1]/div/div/div/div/form/li/input')
search.send_keys("Oversize", Keys.ENTER)
sleep(2)

driver.quit()