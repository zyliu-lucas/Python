from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#创建driver对象
driver = webdriver.Chrome()

#打开百度网站
driver.get('http://www.baidu.com')
sleep(1)
#最大化网页窗口
driver.maximize_window()
sleep(1)
#搜索框输入‘网易云音乐’
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('网易云音乐')
sleep(1)
#点击 ‘百度一下’
driver.find_element_by_xpath('//input[@id="su"]').click()
sleep(1)
#点击‘网易云音乐’进入官网
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]/em').click()
sleep(1)
#点击网易云音乐登录按钮
driver.find_element(By.XPATH,'xpath=//*[text="登录"]').click()
sleep(1)



#在百度搜索结果中点击网易云音乐后，跳转到新打开的网易云音乐页面，需要切换句柄，否则无法定位元素！