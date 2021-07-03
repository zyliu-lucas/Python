from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(2)
driver.maximize_window()
sleep(2)
driver.find_element('id','kw').send_keys('刘晓阳')     #查找元素并输入“刘晓阳”
sleep(2)
driver.find_element('id','su').click()
sleep(5)

driver.quit()       #关闭driver对象