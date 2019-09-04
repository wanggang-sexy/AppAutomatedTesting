#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from handle.login_handle import LoginHandle
import time
import random
from appium.webdriver.common.touch_action import TouchAction
from util.server import Server
from util.log import Logger
from base.swipe_page import SwipePage



class LoginBusiness(object):
    def __init__(self,driver):
        self.driver = driver
        self.login_handle = LoginHandle(self.driver)
        self.swipe_page = SwipePage(self.driver)
        

    def login_judge01(self,i):
        """
        判断启动页面的轮播元素是都存在
        """
        time.sleep(2)
        
        if self.login_handle.judge_launch_page() != None:
            print "u启动轮播元素存在"
            self.swipe_page.swipe_left()
            time.sleep(1)
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            self.swipe_page.swipe_left()
            time.sleep(1)
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            self.swipe_page.swipe_left()
            time.sleep(1)
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            self.swipe_page.swipe_left()
            time.sleep(4)
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"启动轮播元素不存在"


    def login_judge02(self,i):
        """
        进入登录页面判断元素是否存在
        """
        time.sleep(1)
        if self.login_handle.get_title_login() != None:
            print u"登录页面元素存在"
            if self.login_handle.get_right_cancel() !=None:
                print u"取消元素存在"
                time.sleep(1)
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            else:
                print u"取消元素不存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

        else:
            print u"登录页面元素不存在"
            time,sleep(1)
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def login_err01(self,i):
        """
        未输入内容，点击登录按钮
        """
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def login_err02(self,i):
        """
        输入账号，点击登录按钮
        """
        time.sleep(1.5)
        self.login_handle.send_username("13728628610")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def login_err03(self,i):
        """
        输入密码点击登录按钮
        """
        time.sleep(1.5)
        self.login_handle.clear_username()
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def login_err04(self,i):
        """
        密码错误
        """
        time.sleep(1.5)
        self.login_handle.clear_password()
        time.sleep(1.5)
        self.login_handle.send_username("13728628611")
        time.sleep(1.5)
        self.login_handle.send_password("s1234567")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

   
    def login_err05(self,i):
        """
        账号错误
        """
        time.sleep(1.5)
        self.login_handle.send_username('13728628218')
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def login_err06(self,i):
        """
        账户或密码错误5次，锁定账户
        """
        time.sleep(1.5)
        self.login_handle.send_username("13728628611")
        time.sleep(1.5)
        self.login_handle.send_password("s12345")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def login_err07(self,i):
        """
        输入无效账号密码登录
        """
        time.sleep(1.5)
        self.login_handle.send_username("11111111111")
        time.sleep(1.5)
        self.login_handle.send_password("1111111")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

        
    def login_pass01(self,i):
        """
        登录成功,设置手势密码
        """
        time.sleep(1.5)
        self.login_handle.send_username("13728628620")
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(2)
        self.login_handle.click_login()
        time.sleep(5)
        self.gesture_password()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")




    def login_normal(self,i):
        """
        切换普通登录
        """
        time.sleep(1.5)
        self.login_handle.click_normal_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err01(self,i):
        """
        未输入内容，进入普通用户登录
        """
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err02(self,i):
        """
        输入账号，普通登录
        """
        time.sleep(1.5)
        self.login_handle.send_username("TUZCIR")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
    
    def normal_err03(self,i):
        """
        输入密码，普通登录
        """
        time.sleep(1.5)
        self.login_handle.clear_username()
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err04(self,i):
        """
        密码错误，普通登录
        """
        time.sleep(1.5)
        self.login_handle.send_username("MKJAYK")
        time.sleep(1.5)
        self.login_handle.send_password("s123456789")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def normal_err05(self,i):
        """
        账号错误，普通登录
        """
        time.sleep(1.5)
        self.login_handle.send_username("MTIHS")
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err06(self,i):
        """
        账号或密码错误5次，账户锁定
        """
        time.sleep(1.5)
        self.login_handle.send_username("MTIHSQ")
        time.sleep(1.5)
        self.login_handle.send_password("s123456789")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err07(self,i):
        """
        无效账户，普通登录
        """
        time.sleep(1.5)
        self.login_handle.send_username("ABCD")
        time.sleep(1.5)
        self.login_handle.send_password("12345")
        time.sleep(1.5)
        self.login_handle.click_login()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_pass01(self,i):
        """
        普通登录成功，设置手势密码
        """
        time.sleep(2)
        self.login_handle.send_username("MKJAYK")
        time.sleep(2)
        self.login_handle.send_password("s123456")
        time.sleep(2)
        self.login_handle.click_login()
        time.sleep(5)
        self.gesture_password()
        time.sleep(1)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def close_start_app(self,i):
        """
        杀掉APP进程，再次启动APP
        """
        Server().kill_app(i)
        time.sleep(2)
        Server().get_start_app(i)
        time.sleep(2)

    def click_click_account(self):
        """
        点击账户
        """
        self.login_handle.click_account()



    def gesture_password(self):
        """
        设置手势密码
        """
        data = self.get_element_size()
        if self.login_handle.get_get_set_new_password() != None:
            print u"新手设置手势密码元素存在"
            TouchAction(self.driver).press(x=data[0][0], y=data[0][1]).move_to(x=data[1], y=0).wait(1000).move_to(x=data[2], y=0).wait(1000).move_to(x=0, y=data[1]).wait(1000).move_to(x=0, y=data[2]).wait(1000).release().perform()
            time.sleep(1)
            if self.login_handle.get_get_confirm_new_password() != None:
                print u"确认手势密码元素存在"
                time.sleep(1)
                TouchAction(self.driver).press(x=data[0][0], y=data[0][1]).move_to(x=data[1], y=0).wait(1000).move_to(x=data[2], y=0).wait(1000).move_to(x=0, y=data[1]).wait(1000).move_to(x=0, y=data[2]).wait(1000).release().perform()
            else:
                print u"确认手势密码元素不存在"
        else:
            print u"新手设置手势密码元素不存在"
    
   
    def manual_password_unlock(self):
        """
        手势密码解锁
        """
        data = self.get_element_size()
        if self.login_handle.get_get_forget_gesture_password() != None:
            TouchAction(self.driver).press(x=data[0][0], y=data[0][1]).move_to(x=data[1], y=0).wait(1000).move_to(x=data[2], y=0).wait(1000).move_to(x=0, y=data[1]).wait(1000).move_to(x=0, y=data[2]).wait(1000).release().perform()
            
        else:
            print u"忘记手势密码元素不存在"



    def judge_bounced(self,i):
        """
        判断弹窗，是否存在
        """
        time.sleep(3)
        if self.login_handle.get_judge_logibn_bounced() != None:
            print u"弹框元素存在"
            self.login_handle.click_logibn_bounced()
            time.sleep(0.7)
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"弹框元素不存在"
            time.sleep(0.7)
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def login_err08(self,i):
        """
        从登录页面返回首页
        """
        self.login_handle.click_cancel()
        time.sleep(2)
        if self.login_handle.judge_account() != None:
            print u"账户元素存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"账户元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            time.sleep(3)

    def login_err09(self,i):
        """
        输入手机号码，点击取消返回首页
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        self.login_handle.send_username("13728628611")
        time.sleep(1.5)
        self.login_handle.click_cancel()
        time.sleep(2)
        if self.login_handle.judge_account() != None:
            print u"账户元素存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"账户元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def login_err10(self,i):
        """
        输入密码，点击取消返回首页
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(1.5)
        self.login_handle.click_cancel()
        time.sleep(2)
        if self.login_handle.judge_account() != None:
            print u"账户元素存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"账户元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def login_err11(self,i):
        """
        输入手机号码和密码，点击取消返回首页
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        self.login_handle.send_username("13728628611")
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(1.5)
        self.login_handle.click_cancel()
        time.sleep(2)
        if self.login_handle.judge_account() != None:
            print u"账户元素存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"账户元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def login_err12(self,i):
        """
        输入手机和密码，切后台，5s，启动APP，数据存在
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        self.login_handle.send_username("13728628611")
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(1)
        Server().cut_background(i)
        time.sleep(6)
        Server().get_start_app(i)
        time.sleep(6)
        if self.login_handle.get_title_login() != None:
            print u"登录账号元素存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"登录账号元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        self.login_handle.click_cancel()

    def login_err13(self,i):
        """
        输入手机和密码，杀掉进程，启动，数据不存在
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        self.login_handle.send_username("13728628611")
        time.sleep(1.5)
        self.login_handle.send_password("s123456")
        time.sleep(1)
        Server().kill_app(i)
        time.sleep(6)
        Server().get_start_app(i)
        time.sleep(6)
        self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        self.login_handle.click_account()
        time.sleep(1)
        if self.login_handle.get_title_login() != None:
            print u"登录账号元素存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            self.login_handle.click_cancel()
        else:
            print u"登录账号元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err08(self):
        """
        普通登录返回首页
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        if self.login_handle.get_title_login() != None:
            print u"登录账号元素存在"
            time.sleep(1.5)
            self.login_handle.click_cancel()
            time.sleep(3)
            if self.login_handle.judge_account() != None:
                print u"账户元素存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            else:
                print u"账户元素不存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"登录账号元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def normal_err09(self,i):
        """
        输入用户名，返回首页
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        if self.login_handle.get_title_login() != None:
            print u"登录账号元素存在"
            time.sleep(1.5)
            self.login_handle.send_username("13728628613")
            time.sleep(1.5)
            self.login_handle.click_cancel()
            time.sleep(3)
            if self.login_handle.judge_account() != None:
                print u"账户元素存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            else:
                print u"账户元素不存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"登录账号元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err10(self,i):
        """
        输入密码，返回首页
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        if self.login_handle.get_title_login() != None:
            print u"登录账号元素存在"
            time.sleep(1.5)
            self.login_handle.send_password("s123456789")
            time.sleep(1.5)
            self.login_handle.click_cancel()
            time.sleep(3)
            if self.login_handle.judge_account() != None:
                print u"账户元素存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            else:
                print u"账户元素不存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"登录账号元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err11(self,i):
        """
        输入用户名和密码，返回首页
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        if self.login_handle.get_title_login() != None:
            print u"登录账号元素存在"
            time.sleep(1.5)
            self.login_handle.send_password("13728628613")
            time.sleep(1.5)
            self.login_handle.send_password("s123456789")
            time.sleep(1.5)
            self.login_handle.click_cancel()
            time.sleep(3)
            if self.login_handle.judge_account() != None:
                print u"账户元素存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            else:
                print u"账户元素不存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"登录账号元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err12(self,i):
        """
        输入用户名和密码,切后台，等待5s，在启动，数据存在
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        if self.login_handle.get_title_login() != None:
            print u"登录账号元素存在"
            time.sleep(1.5)
            self.login_handle.send_password("13728628613")
            time.sleep(1.5)
            self.login_handle.send_password("s123456789")
            time.sleep(1.5)
            Server().cut_background(i)
            time.sleep(6)
            Server().get_start_app(i)
            time.sleep(6)
            self.login_handle.click_cancel()
            time.sleep(2)
            if self.login_handle.judge_account() != None:
                print u"账户元素存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            else:
                print u"账户元素不存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"登录账号元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

    def normal_err13(self,i):
        """
        输入用户名和密码，杀掉进程，在启动，数据不存在，默认显示登录页面
        """
        time.sleep(1.5)
        self.login_handle.click_account()
        time.sleep(1.5)
        if self.login_handle.get_title_login() != None:
            print u"登录账号元素存在"
            time.sleep(1.5)
            self.login_handle.send_password("13728628613")
            time.sleep(1.5)
            self.login_handle.send_password("s123456789")
            time.sleep(1.5)
            Server().kill_app(i)
            time.sleep(6)
            Server().get_start_app(i)
            time.sleep(6)
            if self.login_handle.judge_account() != None:
                print u"账户元素存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
            else:
                print u"账户元素不存在"
                self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
        else:
            print u"登录账号元素不存在"
            self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


    def get_element_size(self):
        """
        获取手势密码框尺寸
        """
        time.sleep(5)
        lock_pattern = self.login_handle.get_get_gestures_password()
        x = lock_pattern.location.get('x')
        y = lock_pattern.location.get('y')
        width = lock_pattern.size.get('width')
        height = lock_pattern.size.get('height')
        #print(x, y, width, height)
        offset = width / 6 
        p11 = int(x + width / 6), int(y + height / 6)#第一个点
        p12 = int(x + width / 2), int(y + height / 6)#第二个点
        p13 = int(x + width - offset), int(y + height / 6)#第三个点
        p21 = int(x + width / 6), int(y + height / 2)#第四个点
        p22 = int(x + width / 2), int(y + height / 2)#第五个点
        p23 = int(x + width - offset), int(y + height / 2)#第六个点
        p31 = int(x + width / 6), int(y + height - offset)#第七个点
        p32 = int(x + width / 2), int(y + height - offset)#第八个点
        p33 = int(x + width - offset), int(y + height - offset)#第九个点
        p2 = p12[0] - p11[0]#偏移量
        p3 = p13[0] - p12[0]#偏移量
        return p11,p2,p3



if __name__ == "__main__":
    login = LoginBusiness(0)
    login.login_pass()