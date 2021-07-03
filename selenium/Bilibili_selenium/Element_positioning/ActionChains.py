#携程帐号注册
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#打开浏览器，加载携程注册界面
driver = webdriver.Chrome()
driver.get('https://passport.ctrip.com/user/reg/home')
sleep(2)
#最大化网页窗口
driver.maximize_window()
sleep(1)

#点击‘同意并继续’
driver.find_element_by_xpath('//*[@id="agr_pop"]/div[3]/a[2]').click()

#定位滑块的位置
element_hk = driver.find_element_by_css_selector('div.cpt-drop-box>div.cpt-drop-btn')
print(element_hk.size['width'],element_hk.size['height'])

#定位滑块条的位置
element_cao = driver.find_element_by_css_selector('div.cpt-drop-box>div.cpt-bg-bar')
print(element_cao.size['width'],element_cao.size['height'])

#实现滑块操作
x_location = element_hk.size['width']+element_cao.size['width']
y_location = element_cao.size['height']
ActionChains(driver).drag_and_drop_by_offset(element_hk,x_location,y_location).perform()
sleep(1)
#driver.close()

#淘宝网鼠标移动操作
#driver2 = webdriver.Chrome()
#driver2.get('https://www.taobao.com/')
#sleep(2)

#最大化网页窗口
#driver2.maximize_window()
#sleep(1)

#鼠标移动到中国大陆位置
#element_1 = driver2.find_element_by_css_selector("div.site-nav-menu-hd>span.site-nav-region")
#ActionChains(driver2).move_to_element(element_1).perform()
#element_2 = driver2.find_element_by_css_selector("div.site-nav-menu-bd.site-nav-menu-list>ul#J_SiteNavRegionList>li:nth-child(3)")
#element_2.click()
#sleep(2)



#携程网的滑块操作没有实现滑块拖动！