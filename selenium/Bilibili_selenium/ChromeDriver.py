from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep

wb = WebDriver(executable_path='chromedriver')   #创建webdriver对象
sleep(1)
wb.maximize_window()
sleep(2)

wb.execute('get',{'url':'http://www.baidu.com'})   #访问URL
sleep(2)

#定位到文本框进行输入
el = wb.execute('findElement',{
    'using': By.XPATH,
    'value': '//input[@id="kw"]'})['value']
el._execute('sendKeysToElement',{
    'text': '小龙女',
    'value':''})
sleep(1)

#定位到 百度一下 按钮，进行点击
el1 = wb.execute('findElement',{
    'using': By.XPATH,
    'value':'//input[@id="su"]'})['value']
el1._execute('clickElement')
sleep(5)

wb.quit()   #关闭driver对象