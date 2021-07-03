from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains      #导入ActionChains类

dr = webdriver.Chrome()
dr.get('http://www.baidu.com')
sleep(2)
dr.maximize_window()             #将浏览器窗口最大化
sleep(2)

#第一步：先找到鼠标操作的元素
ele = dr.find_element_by_xpath('//[@id="u1"]/[@name="tj_settingicon"]')
#第二步：实例化ActionChains类
ac = ActionChains(dr)
#第三步：将鼠标操作的元素添加到actions列表中，使用move_to_element()方法
ac.move_to_element(ele)
#第四步：调用preform()方法来执行鼠标操作
ac.perform()


#setting = dr.find_element_by_link_text("设置")
#ActionChains(dr).move_to_element(setting).perform()
#sleep(2)
#dr.find_element_by_link_text("搜索设置").click()
#sleep(3)



#操作失败！！！