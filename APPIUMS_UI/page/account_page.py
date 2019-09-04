#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from util.get_by_local import GetByLocal
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
class AccountPage(object):
	def __init__(self,driver):
		self.driver = driver
		self.get_by_local = GetByLocal(self.driver)

	def get_account_page_title(self):
		"""
		获取账户中心元素
		"""
		return self.get_by_local.get_element("account_page_title","account_page_element")


	def get_account_page_head_portrait(self):
		"""
		获取账户头像元素
		"""
		return self.get_by_local.get_element("account_page_head_portrait","account_page_element")

	def get_account_page_msg(self):
		"""
		获取消息元素
		"""
		return self.get_by_local.get_element("account_page_msg","account_page_element")

	def get_account_page_setting(self):
		"""
		获取右上角设置元素
		"""
		return self.get_by_local.get_element("account_page_setting","account_page_element")

	def get_account_page_recharge(self):
		"""
		充值元素
		"""
		return self.get_by_local.get_element("account_page_recharge","account_page_element")

	def get_account_page_withdrawal(self):
		"""
		提现元素
		"""
		return self.get_by_local.get_element("account_page_withdrawal","account_page_element")

	def get_account_page_recommended_prize(self):
		"""
		推荐有奖元素
		"""
		return self.get_by_local.get_element("account_page_recommended_prize","account_page_element")

	def get_account_page_sign(self):
		"""
		我要签到元素
		"""
		return self.get_by_local.get_element("account_page_sign","account_page_element")

	def get_account_page_directory(self):
		"""
		账户目录信息(包含：账户总览，资金明细，我的出借，我的借款，回款日历，我的优惠券，会员中心，客服热线)元素
		"""
		return self.get_by_local.get_element("account_page_directory","account_page_element")

	def get_account_page_return(self):
		"""
		个人设置页面左上角返回按钮元素
		"""
		return self.get_by_local.get_element("account_page_return","account_page_element")

	def get_account_page_personal_settings(self):
		"""
		个人设置页面顶部title元素
		"""
		return self.get_by_local.get_element("account_page_personal_settings","account_page_element")

	def get_account_page_personal_settings_head_portrait(self):
		"""
		个人设置页面头像元素
		"""
		return self.get_by_local.get_element("account_page_personal_settings_head_portrait","account_page_element")

	def get_account_page_email_identif(self):
		"""
		邮箱认证元素
		"""
		return self.get_by_local.get_element("account_page_email_identif","account_page_element")

	def get_account_page_realname_identif(self):
		"""
		实名认证元素
		"""
		return self.get_by_local.get_element("account_page_realname_identif","account_page_element")

	def get_account_page_my_bank(self):
		"""
		我的银行卡元素
		"""
		return self.get_by_local.get_element("account_page_my_bank","account_page_element")

	def get_account_page_modify_password(self):
		"""
		修改登录密码元素
		"""
		return self.get_by_local.get_element("account_page_modify_password","account_page_element")

	def get_account_page_trade_password(self):
		"""
		设置交易密码元素
		"""
		return self.get_by_local.get_element("account_page_trade_password","account_page_element")

	def get_account_page_gestures_password(self):
		"""
		修改手势密码元素
		"""
		return self.get_by_local.get_element("account_page_gestures_password","account_page_element")

	def get_account_page_loginout(self):
		"""
		安全退出元素
		"""
		return self.get_by_local.get_element("account_page_loginout","account_page_element")