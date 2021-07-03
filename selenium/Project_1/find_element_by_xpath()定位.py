from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_xpath("//input[@id='kw' and @class='s_ipt' and @name='wd']").send_keys('云顶之奕黑暗装备')
sleep(3)
driver.maximize_window()             #将浏览器窗口最大化
sleep(3)
driver.set_window_size(500,600)      #将浏览器窗口设置固定大小
sleep(3)

driver.quit()