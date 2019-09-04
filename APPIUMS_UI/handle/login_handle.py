#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from page.login_page import LoginPage


class LoginHandle(object):
    """
    操作登录页面元素
    """
    def __init__(self,driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def judge_launch_page(self):
        """
        判断启动页面的轮播图元素是否存在
        """
        return self.login_page.get_launch_page_element()

    def judge_account(self):
        """
        判断账户元素是否存在
        """
        return self.login_page.get_account_element()

    def get_title_login(self):
        """
        判断登录页面title元素是否存在
        """
        return self.login_page.get_login_title_element()

    def get_judge_logibn_bounced(self):
        """
        判断启动或者登录弹框
        """
        return self.login_page.get_login_bounced()

    def click_logibn_bounced(self):
        """
        关闭登录弹框
        """
        self.login_page.get_login_bounced().click()

    def get_right_cancel(self):
        """
        判断右上角取消按钮元素是否存在
        """
        return self.login_page.get_login_right_element()

    def send_username(self,user):
        """
        输入手机号码及用户名
        """
        self.login_page.get_uernsme_element().send_keys(user)

    def clear_username(self):
        """
        清除手机号码
        """
        self.login_page.get_uernsme_element().clear()

    def send_password(self,password):
        """
        输入登录密码
        """
        self.login_page.get_password_element().send_keys(password)

    def clear_password(self):
        """
        清除登录密码
        """
        self.login_page.get_password_element().clear()

    def click_login(self):
        """
        点击登录按钮
        """
        self.login_page.get_login_button_element().click()

    def click_normal_login(self):
        """
        点击切换普通登录
        """
        self.login_page.get_normal_login_element().click()

    def click_free_registration(self):
        """
        点击免费注册按钮
        """
        self.login_page.get_free_registration_element().click()

    def click_cancel(self):
        """
        点击取消按钮
        """
        self.login_page.get_cancel_element().click()

    def click_forgot_password(self):
        """
        点击忘记密码按钮
        """
        self.login_page.get_forgot_password_element().click()

    def click_account(self):
        """
        点击账户按钮
        """
        self.login_page.get_account_element().click()

    def get_fail_toast(self,message):
        """
        获取toast，根据返回信息进行反数据，5.0以上手机可用,appium版本1.7
        """
        toast_element = self.login_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False

    def get_get_gestures_password(self):
        """
        手势密码框元素
        """
        return self.login_page.get_gestures_password()


    def get_get_set_new_password(self):
        """
        设置新手势密码
        """
        return self.login_page.get_set_new_password()

    def get_get_confirm_new_password(self):
        """
        确认手势密码
        """
        return self.login_page.get_confirm_new_password()

    def get_get_two_password_mismatch(self):
        """
        两次密码不一致
        """
        return self.login_page.get_two_password_mismatch()

    def get_get_forget_gesture_password(self):
        """
        忘记密码
        """
        return self.login_page.get_forget_gesture_password()
        


if __name__ == "__main__":
    loginhadle = LoginHandle(0)
    print LoginHandle.click_account()