from selenium import webdriver
from time import  sleep
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(2)
driver.maximize_window()             #将浏览器窗口最大化
sleep(2)
#driver.find_element_by_css_selector("input#kw").send_keys("云顶之奕黑暗装备")
driver.find_element_by_css_selector("input.s_ipt").send_keys("云顶之奕黑暗装备")
sleep(2)
driver.quit()

#在css定位中，id简写用"#"来表示，class属性简写用“.”来表示