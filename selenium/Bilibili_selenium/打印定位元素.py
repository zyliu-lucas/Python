from selenium import webdriver

#创建driver对象
driver = webdriver.Chrome()
#最大化窗口
driver.maximize_window()

#打开百度网站
driver.get('http://www.baidu.com')

#定位元素
dr = driver.find_element_by_partial_link_text('百度').text
#打印元素
print(dr)


'''
定位到多个相同元素，取其中的某个元素：
    1.drivrt.find_elements_by_partial_link_text('百度')[1].text      --定位第二个‘百度’元素

遍历找到的‘百度’元素：
    dr = driver.find_elements_by_partial_link_text('百度')    
    for i in dr:
        print(i.text)
'''