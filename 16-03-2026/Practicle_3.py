from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)

driver.get("https://www.flipkart.com/")
sleep(10)
cross = driver.find_element(By.XPATH, "//span[@role='button']")
cross.click()

search = driver.find_element(By.NAME, 'q')
search.send_keys("Mobiles", Keys.ENTER)
sleep(4)

apple = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[2]/div[2]/div[1]/div[3]/div/label/div[1]')
apple.click()
sleep(4)

img = driver.find_element(By.XPATH, "//div[@class='lWX0_T']/img[1]")
print(img.get_attribute('src'))


driver.quit()