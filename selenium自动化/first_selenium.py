#打开百度首页
from selenium import webdriver
driver = webdriver.Firefox()
url = 'https://www.baidu.com/'
driver.get(url)
#打开get就类似于在浏览器地址栏里面放入网址
driver.quit()#退出浏览器