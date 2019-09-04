# -*- coding: utf-8 -*-
'''
import hashlib,time
import requests

def Md5Enerypt(Lstr):
    m = hashlib.md5()
    m.update(str(Lstr))
    return m.hexdigest()
#PC端注册
def pc_registration():
        url = 'http://183.62.205.226:8777/hsdgold-portal-pc/registerUser.do'
        for i in range(18888880650,18888885001):
                datd = {'mobilePhone':str(i),
                'loginPassword':'14e1b600b1fd579f47433b88e8d85291',
                'smsCode':'123456',
                'code_id':Md5Enerypt(str(i))}
                res = requests.post(url=url,data=datd)
                print res.text


if __name__ == "__main__":
    pc_registration()

'''
'''
import unittest
from BeautifulReport import BeautifulReport


class UnittestCaseSecond(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""
    
    def test_equal(self):
        """
            test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)
    
    @BeautifulReport.add_test_img('测试报告.png')
    def test_is_none(self):
        """
            test None object
        :return:
        """
        save_some_img('测试报告.png')
        self.assertIsNone(None)

'''

# coding:utf-8
# 上传模块
from selenium import webdriver
from time import sleep

# 使用谷歌浏览器打开一个网页
browser = webdriver.Chrome()
sleep(2)
browser.get("https://tester.cloudcubic.net/login.aspx")
browser.maximize_window()

# 定位登录框
sleep(5)
browser.find_element_by_id("txtUserName").send_keys("huge")
sleep(5)
browser.find_element_by_id("txtPassWord").send_keys("123456")
sleep(5)
browser.find_element_by_id("submitlogin").click()

# 定位无纸化办公流程设置
sleep(5)
browser.find_element_by_xpath("//*[@id='global_channel_tree5']/li[2]/div/span").click()
sleep(5)
browser.find_element_by_xpath("//*[@id='global_channel_tree5']/li[2]/ul/li[2]/div/span").click()
sleep(5)
x_frame1 = browser.find_element_by_xpath("//*[@name='151']")
browser.switch_to.frame(x_frame1)
browser.find_element_by_id("btn-add").click()

browser.switch_to.frame(0)
sleep(5)
browser.find_element_by_xpath("//*[@id='name']").send_keys(u"原材料审核")
sleep(5)
browser.find_element_by_xpath("//*[@id='workFlow']/span/span").click()#对应表单

sleep(5)
browser.find_element_by_xpath("//*[@id='COMBO_WRAP']/div[2]/div/div[2]").click()#选择设计部请假单

sleep(5)

browser.find_element_by_xpath("//*[@id='billType']/span/span").click()#归档类别

sleep(5)
browser.find_element_by_xpath("//*[@id='COMBO_WRAP']/div[3]/div/div[2]").click()#选择行政管理

sleep(5)
browser.find_element_by_xpath("//*[@id='filter-filer']/span").click()#选择归档人



# 选择归档人
sleep(10)
x_frame2 = browser.find_element_by_xpath("//*[@name='JDG15314629005062']")
browser.switch_to.frame(x_frame2)
browser.find_element_by_xpath("//*[@id='2']/td[1]").click()# 这里的定位有点问题，好像定位不到，其他的都已ok
sleep(5)
browser.find_element_by_class_name("ui_state_highlight1").click()
sleep(10)

