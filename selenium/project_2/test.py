#-*- coding:utf-8 -*-
#@time : 2021/6/19 11:35
#@Author : zyliu

from selenium import webdriver

#webdriver实例化
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

