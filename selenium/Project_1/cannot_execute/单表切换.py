from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
sleep(3)
driver.maximize_window()
sleep(2)
driver.switch_to.frame("login_frame")
driver.find_element_by_name('email').send_keys('username')
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_name('login_button').click()
driver.switch_to.default_content()