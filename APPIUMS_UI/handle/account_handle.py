#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from page.account_page import AccountPage

class AccountHandle(object):
	def __init__(self,driver):
		self.driver = driver
		self.account_page = AccountPage(self.driver)

	def judge_account_page_title(self):
		"""
		判断账户中心元素是否存在
		"""
		return self.account_page.get_account_page_title()

	def click_account_page_head_portrait(self):
		"""
		点击账户中心头像
		"""
		self.account_page.get_account_page_head_portrait().click()

	def click_account_page_msg(self):
		"""
		点击账户中心消息
		"""
		self.account_page.get_account_page_msg().click()

	def click_account_page_setting(self):
		"""
		点击右上角设置按钮
		"""
		self.account_page.get_account_page_setting().click()

	def click_account_page_recharge(self):
		"""
		点击充值按钮
		"""
		self.account_page.get_account_page_recharge().click()

	def click_account_page_withdrawal(self):
		"""
		点击提现按钮
		"""
		self.account_page.get_account_page_withdrawal().click()

	def click_account_page_recommended_prize(self):
		"""
		点击推荐有奖按钮
		"""
		self.account_page.get_account_page_recommended_prize().click()

	def click_account_page_sign(self):
		"""
		点击我要签到按钮
		"""
		self.account_page.get_account_page_sign().click()

	def click_account_page_directory(self,n):
		"""
		点击账户目录信息(包含：账户总览，资金明细，我的出借，我的借款，回款日历，我的优惠券，会员中心，客服热线)元素
		"""
		elements = self.account_page.get_account_page_directory()
		elements[n].click()

	def click_account_page_return(self):
		"""
		点击个人设置左上角返回按钮
		"""
		self.account_page.get_account_page_return().click()

	def judge_account_page_personal_settings(self):
		"""
		判断个人设置页面title
		"""
		return self.account_page.get_account_page_personal_settings()

	def click_account_head_portrait(self):
		"""
		点击个人设置头像
		"""
		self.account_page.get_account_page_personal_settings_head_portrait().click()

	def click_account_page_email_identif(self):
		"""
		点击邮箱认证
		"""
		self.account_page.get_account_page_email_identif().click()

	def click_account_page_realname_identif(self):
		"""
		点击实名认证
		"""
		self.account_page.get_account_page_realname_identif().click()

	def click_account_page_my_bank(self):
		"""
		点击我的银行卡
		"""
		self.account_page.get_account_page_my_bank().click()

	def click_account_page_modify_password(self):
		"""
		点击修改登录密码
		"""
		self.account_page.get_account_page_modify_password().click()

	def click_account_page_trade_password(self):
		"""
		点击交易密码
		"""
		self.account_page.get_account_page_trade_password().click()

	def click_account_page_gestures_password(self):
		"""
		点击手势密码
		"""
		self.account_page.get_account_page_gestures_password().click()

	def click_account_page_loginout(self):
		"""
		点击安全退出
		"""
		self.account_page.get_account_page_loginout().click()