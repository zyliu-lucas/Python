'''
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
'''


from selenium.webdriver.chrome.webdriver import WebDriver
#from selenium import webdriver
from time import sleep

wb = WebDriver(executable_path = 'chromedriver')

wb.execute('get',{'url':'http://www.baidu.com'})
sleep(2)
wb.maximize_window()
sleep(2)

el = wb.execute('findElement',{
    'using':'xpath',
    'value':'//input[@id="kw"]'})['value']
el._execute('sendKeysToElement',{
    'text':'珠光护手',
    'value':''})
el1 = wb.execute('findElement',{
    'using':'xpath',
    'value':'//input[@id="su"]'})['value']
el1._execute('clickElement')
sleep(3)

wb.quit()       #关闭driver对象