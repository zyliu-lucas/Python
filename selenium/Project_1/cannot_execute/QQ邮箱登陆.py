# -*- coding:utf-8 -*-
# QQ邮箱登录

from selenium import webdriver
import time

first_url = 'http://www.mail.qq.com'
driver = webdriver.Chrome()
driver.get(first_url)
driver.implicitly_wait(10)
driver.maximize_window()

# 切换到iframe
time.sleep(3)
driver.switch_to.frame(driver.find_element_by_id('login_frame'))
time.sleep(3)

# 点击头像进行登录
driver.find_element_by_id('img_out_1********2').click()

# 进入收件箱
driver.find_element_by_id('folder_1').click()

# 点击写信
driver.find_element_by_id('composebtn').click()

time.sleep(3)
# 切换到iframe
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
frame = driver.find_element_by_id('mainFrame')
driver.switch_to.frame(frame)

time.sleep(3)
# 输入收件人
# driver.find_element_by_class_name('js_input').send_keys('********@qq.com')
driver.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input").send_keys('*******@qq.com')
# 添加附件
driver.find_element_by_name('UploadFile').send_keys(r'D:\Test\text.docx')

# 输入正文，先切入到iframe
driver.switch_to_frame(driver.find_element_by_class_name('qmEditorIfrmEditArea'))
time.sleep(3)
# 输入正文
driver.find_element_by_xpath("/html/body").send_keys('gggg')

# 切出iframe
driver.switch_to_default_content()

# 再切入到‘发送’按钮的iframe
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))

time.sleep(3)
# 邮件发送
driver.find_element_by_name('sendbtn').click()