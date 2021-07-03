#打开百度首页
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
sleep(2)
driver.maximize_window()
sleep(2)

driver.quit()       #关闭driver对象