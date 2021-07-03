'''
    封装SeleniumLibrary关键字库，将常用的selenium关键字全部进行封装
'''
from selenium import webdriver
import time



#构建浏览器对象
def open_browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print (e)
        driver = webdriver.Chrome()
    return driver

class SeleniumKey:
    #构造函数
    def __init__(self, type_):
        self.driver = open_browser(type_)

    # 访问URL
    def open(self, text):
        self.driver.get(text)

    #元素定位
    def locator(self, name, value):
        return self.driver.find_element(name, value)

    #点击
    def click(self, name, value):
        self.locator(name, value).click()

    #输入
    def input(self, name, value, text):
        self.locator(name, value).send_keys(text)

    #浏览器关闭
    def quit(self):
        self.driver.quit()

    #强制等待
    def sleep(self, text):
        self.sleep(text)