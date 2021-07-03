from selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner

class shoptest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.get('http://39.98.138.157/shopxo/index.php')

    def test_login(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[1]/input').send_keys('666666')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input').send_keys('111111')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
    def tearDown(self):
        self.driver.quit()

if __name__ =='__main__':
    test = unittest.TestSuite()
    test.addTest(shoptest('test_login'))
    file_result = open(r'c:\a.html','wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u'webTourTest测试报告',description=u'用例执行情况')
    runner.run(test)
    file_result.close()


