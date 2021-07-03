from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.get("https://www.jianshu.com/sign_in")
t.sleep(3)
driver.maximize_window()
t.sleep(3)

js_register = 'document.getElementById("js-sign-up-btn").click()'   #单击‘注册’按钮
driver.execute_script(js_register)
t.sleep(3)

driver.quit()