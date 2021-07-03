import unittest
from time import sleep
from ddt import ddt, data, unpack
from test_keywords_demo import TestKeyWords #导入同一文件夹下的Python文件中的自定义模块
#from web_ui.test_keywords_demo import TestKeyWords

@ddt
class TestForKey(unittest.TestCase):
    #前置条件
    def setUp(self) -> None:
        self.tk = TestKeyWords('http://www.baidu.com','chrome')

    #后置条件
    def tearDown(self) -> None:
        self.tk.quit_browser()

    #测试用例1
    @data(['id','九神盾战士'],['id','九圣光护卫'])
    @unpack
    def test_1(self,locator,input_value):
        self.tk.input_text(locator,'kw',input_value)
        self.tk.click_element('id','su')
        sleep(3)

    # #测试用例2
    # def test_2(self,e):
    #     self.tk.input_text('id','kw','九圣光护卫')
    #     self.tk.click_element('id','su')
    #     sleep(3)

if __name__ == '__main__':
    unittest.main()