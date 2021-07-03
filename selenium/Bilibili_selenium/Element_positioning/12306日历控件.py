from selenium import webdriver
import time

driver = webdriver.Chrome()
#打开12306网站
driver.get('https://www.12306.cn/index')
time.sleep(3)
#最大化网页窗口
driver.maximize_window()
time.sleep(1)

'''
#通过selenium方式来实现
#点击日历控件
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div/i").click()
time.sleep(2)
#点击具体日期(2021-06-25)
driver.find_element_by_xpath("/html/body/div[10]/div[1]/div[2]/div[25]/div").click()
time.sleep(2)
'''

'''通过JS方式来实现
js = "documenet.getElementById('train_date').value='2021-06-15'" #需要执行的js脚本
driver.execute_script(js)
time.sleep(2)
#driver.quit()

第24行代码报错，无法执行。

'''