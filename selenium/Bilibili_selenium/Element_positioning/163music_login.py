from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#创建driver对象
driver = webdriver.Chrome()

#打开百度网站
driver.get('https://music.163.com/')
sleep(1)

#最大化网页窗口
driver.maximize_window()
sleep(1)

#点击网易云音乐登录按钮
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/a").click()
sleep(2)

#点击“选择其他登录模式”
driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[2]/div/div[3]/a").click()
sleep(2)

#勾选同意服务条款
driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]/div[1]/div[3]/input").click()
sleep(1)
#点击“QQ登录”按钮
driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]/div[1]/div[2]/ul/li[2]/a").click()
sleep(1)

#跳转到QQ登录页面需要切换句柄

#退出浏览器
#driver.quit()