#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from util.get_by_local import GetByLocal
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(object):
    #获取登录页面所有的页面元素信息
    def __init__(self,driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)
        '''
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)
        '''

    def get_launch_page_element(self):
        """
        获取启动页面的轮播图
        """
        return self.get_by_local.get_element("launch_page","launch_page_element")
        
    def get_login_title_element(self):
        """
        获取登录title页面元素
        """
        return self.get_by_local.get_element("mobile_login","login_element")

    def get_login_bounced(self):
        """
        登录后出现弹窗
        """
        return self.get_by_local.get_element("login_bounced","login_element")

    def get_login_right_element(self):
        """
        获取右上角取消按钮
        """
        return self.get_by_local.get_element("cancel","login_element")

    def get_uernsme_element(self):
        """
        获取手机及用户名登录元素信息
        """
        return self.get_by_local.get_element("mobile_login","login_element")
    def get_password_element(self):
        """
        获取登录密码元素信息
        """
        return self.get_by_local.get_element("mobile_login_password","login_element")
    def get_login_button_element(self):
        """
        获取登录按钮元素信息
        """
        return self.get_by_local.get_element("login_buttion","login_element")
    def get_forgot_password_element(self):
        """
        获取忘记登录密码元素信息
        """
        return self.get_by_local.get_element("forgot_password","login_element")
    def get_normal_login_element(self):
        """
        普通登录元素
        """
        return self.get_by_local.get_element("normal_login","login_element")
    def get_free_registration_element(self):
        """
        免费注册元素
        """
        return self.get_by_local.get_element("free_registration","login_element")
    def get_cancel_element(self):
        """
        取消按钮元素信息
        """
        return self.get_by_local.get_element("cancel","login_element")
    def get_account_element(self):
        """
        获取账户按钮元素信息
        """
        return self.get_by_local.get_element("account","login_element")
    def get_toast_element(self,message):
        """
        获取toast元素信息,5.0以上手机可用
        """
        time.sleep(2)
        toast_element = ("xpath","//*[contains(@text,'+message+')]")
        return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(toast_element))

    def get_gestures_password(self):
        """
        获取手势密码框元素
        """
        return self.get_by_local.get_element("gestures_password","login_element")

    def get_set_new_password(self):
        """
        设置新手手势密码
        """
        return self.get_by_local.get_element("set_new_password","login_element")

    def get_confirm_new_password(self):
        """
        确认手势密码
        """
        return self.get_by_local.get_element("confirm_new_password","login_element")

    def get_two_password_mismatch(self):
        """
        两次密码不一致
        """
        return self.get_by_local.get_element("two_password_mismatch","login_element")

    def get_forget_gesture_password(self):
        """
        忘记手势密码
        """
        return self.get_by_local.get_element("forget_gesture_password","login_element")





    
if __name__ == "__main__":

    baee = BaseDriver()
    driver = baee.android_driver(0)
    login =  LoginPage(driver)
    print login.get_inverstment()