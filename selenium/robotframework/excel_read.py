'''
excel文件的用例读取驱动
'''
from selenium import webdriver
import openpyxl

#找到excel
from selenium_key封装 import SeleniumKey

excel = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\selenium\robotframework\testcase.xlsx')

#找到对应的sheet页(打印表格sheet页的页名)
for sheet in excel.sheetnames:
    sheet1 = excel[sheet]
    for value in sheet1.values:
        #获取excel中的数据，作为用例的驱动数据
        param = {}
        param['name'] = value[2]
        param['value'] = value[3]
        param['text'] = value[4]
        #每一行参数都可能存在有None值，需要管理获取到的数据内容的正确性
        for key in list(param.keys()):
            if param[key] is None:
                del param[key]
    '''
        用例数据的读取中，会分为两种情况：
            1.正常实现关键字操作行为的内容；
            2.实例化webdriver对象。
    '''
    if type(value[0]) is int:
        if value[1] == 'open_browser':
            sk = SeleniumKey(param['text'])
        else:
            getattr(sk, value[1])(**param)
