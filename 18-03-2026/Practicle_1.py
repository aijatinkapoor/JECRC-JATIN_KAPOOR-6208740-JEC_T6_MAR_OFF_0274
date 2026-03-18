from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)

driver.get("https://www.lenskart.com/sunglasses.html")
sleep(3)

# eye = driver.find_element(By.ID, 'lrd1')
btn = driver.find_element(By.XPATH, '//input[@id="suited_for_id-1"]/parent::div')
btn.click()
sleep(2)

assert btn.is_enabled(), 'False'

# assert "EYE" == eye.text, "Didn't Find"

driver.quit()