from selenium import webdriver
from time import sleep

#打开Chrome浏览器
driver = webdriver.Chrome()
sleep(1)

#打开百度地址
driver.get('http://www.baidu.com')
sleep(1)
#最大化网页窗口
driver.maximize_window()
sleep(1)

#定位百度搜索框：使用绝对路径定位
#driver.find_element_by_css_selector('HTML>body>div>div>div>div>div>form>span>input').send_keys('巨人杀手')   #绝对路径使用‘>’
#driver.find_element_by_css_selector('HTML body div div div div div form span input').send_keys('巨人杀手')   #绝对路径使用‘空格’

#定位百度搜索框：使用 ID 定位，ID选择器符号‘#’
#driver.find_element_by_css_selector('#kw').send_keys('巨人杀手')

#定位百度搜索框：使用 class 定位，class选择器符号‘.’
#driver.find_element_by_css_selector('.s_ipt').send_keys('巨人杀手')

#定位百度搜索框：使用其他属性定位，使用符号‘[属性名=“属性值”]’
#driver.find_element_by_css_selector('[autocomplete="off"]').send_keys("巨人杀手")   #通过一个属性定位
#driver.find_element_by_css_selector('[autocomplete="off"]''[name="wd"]').send_keys("巨人杀手")   #通过两个或多个属性定位

'''定位百度搜索框：通过部分属性值进行定位 "[属性值+匹配符 = '属性值的某字符']"
    匹配符号:
        *   属性值中包含某个字符；
        ^   属性值以某个字符开头；
        $   属性值以某个字符结尾。
'''
#driver.find_element_by_css_selector("[autocomplete*='f']").send_keys("巨人杀手")   #匹配符*
#driver.find_element_by_css_selector("[autocomplete^='o']").send_keys("巨人杀手")   #匹配符^
#driver.find_element_by_css_selector("[autocomplete$='f']").send_keys("巨人杀手")   #匹配符$

#定位百度搜索框：通过标签层级定位
#driver.find_element_by_css_selector("form>span>input").send_keys("巨人杀手")   #层级定位
#driver.find_element_by_css_selector("form#form>span>input").send_keys("巨人杀手")   #层级+form的ID属性组合定位
#driver.find_element_by_css_selector("form.fm>span>input").send_keys("巨人杀手")   #层级+form的class属性组合定位
sleep(1)

#定位百度首页右上方新闻链接：通过兄弟节点定位
#driver.find_element_by_css_selector('#s-top-left > a:nth-child(1)').click()   #定位第一个节点：新闻
#driver.find_element_by_css_selector('#s-top-left > a:first-child').click()   #定位第一个节点：新闻
#driver.find_element_by_css_selector('#s-top-left a:nth-child(2)').click()   #定位第二个节点：hao123;">"用空格代替

#点击 ‘百度一下’
driver.find_element_by_xpath('//input[@id="su"]').click()
sleep(1)



'''
css定位的方法：
    1）。绝对路径：
    2）。ID
    3）。class
    4）。其他属性定位
    5）。部分属性值定位
    6）。通过标签层级定位：'>'或者'空格'；一般会跟ID/class/属性定位一起组合来定位
    7）。通过兄弟节点定位：（兄弟节点指同意父级标签下有多个相同标签的元素）
        定位第一个节点：first-child
        定位第二/三/四/...n个节点：nth-child(n)  --child(n)的n为节点的序号
        定位最后一个节点：last-child
'''