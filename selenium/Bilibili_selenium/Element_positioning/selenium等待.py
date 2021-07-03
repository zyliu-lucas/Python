#导入selenium和WebDriver来实现自动化
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from time import sleep

#通过自动化的方式启用chrome浏览器
#实例化ChromeDriver来对浏览器进行操作
driver = webdriver.Chrome()
#设置隐式等待
#driver.implicitly_wait(10)

#调用浏览器访问指定的URL（百度）
driver.get('http://www.baidu.com')
#sleep(1)

#最大化网页窗口
driver.maximize_window()
#sleep(1)

#在百度搜索框中输入“云顶之奕”，并点击“百度一下”按钮
driver.find_element_by_id("kw").send_keys('云顶之奕')
driver.find_element_by_id('su').click()

#设置强制等待
#sleep(3)
#设置显式等待
#WebDriverWait(driver, 20, 0.5).until(lambda el:driver.find_element_by_xpath('//*[@id="1"]/h3/a'))

#设置显示等待2
location = (By.XPATH,'//*[@id="1"]/h3/a')
WebDriverWait(driver,20,0.5).until(ec.presence_of_element_located(location))

#点击第一条搜索结果
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
sleep(3)

#退出浏览器
driver.quit()

'''
selenium三大等待
    1.强制等待：通过带入time中的sleep，等待X秒后，再继续执行后续代码；缺点是无法精准的把握等待的时间，无法准确判定页面是否加载完成，如果一直使用强制等待，
        会严重影响整个自动化运行的效率。
    2.隐式等待：设置一个隐形的等待，设置最长的等待时间，如果在这个时间内完成了页面的加载，则进行下一步，否则一直等待到时间结束，再进行下一步。优点：对整个WebDriver的周期
        都能够起作用，所以只需要设置一次；缺点：必须要等待整个页面全部加载完成才可以进行下一步操作，有时候页面中的特定元素已经被加载出来，但是页面本身还是没有加载完成。应
        用度上不是太灵活。
    3.显式等待：专门用于对指定的元素进行等待。在设置的最长时间内，依照查找的时间频率来进行搜素，查找指定的对象，until表示如果找到，则继续下一步，否则报出异常NoSuchElementException
        /TimeOut；Until_Not()与Until相反。
        优点：精确对某个特定条件进行等待，不会兰妃对于的时间在等待上。如果条件成立，立即进入下一步。如果不成立则立即抛出异常。
        缺点：应用上而言，相对于其他两种等待更为复杂
'''