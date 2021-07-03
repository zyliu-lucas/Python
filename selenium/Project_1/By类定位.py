from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By   #导入By类
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
sleep(1)
driver.maximize_window()
sleep(1)
driver.find_element(By.ID,'kw').send_keys("彼岸之主")
#driver.find_element(By.ID,'kw').click()
driver.find_element_by_id('su').click()
sleep(5)
driver.quit()