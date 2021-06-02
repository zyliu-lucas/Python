from selenium import webdriver
from selenium.webdriver.common.by import By   #导入By类
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.find_element(By.ID,'kw').send_keys("彼岸之主")
driver.find_element(By.ID,'kw').click()
#driver.quit()