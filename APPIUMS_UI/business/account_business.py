#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from handle.account_handle import AccountHandle
from handle.login_handle import LoginHandle
from util.log import Logger
import time


class AccountBusiness(object):
	def __init__(self,driver):
		self.driver = driver
		self.account_handle = AccountHandle(self.driver)
		self.login_handle = LoginHandle(self.driver)

	def my_account(self,i):
		"""
		我的账户元素是否存在
		"""
		time.sleep(1.5)
		if self.account_handle.judge_account_page_title() != None:
			print u"我的账户元素存在"
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		else:
			print u"我的账户元素不存在"
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
	def login_out_app(self,i):
		"""
		退出APP登录
		"""
		time.sleep(1.5)
		self.account_handle.click_account_page_head_portrait()
		time.sleep(2)
		self.account_handle.click_account_page_loginout()
		time.sleep(1.5)
		if self.login_handle.get_title_login() != None:
			print u"退出APP登录"
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		else:
			print u"退出APP登录失败"
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		time.sleep(5)

	def account_page_account(self,i):
		"""
		判断账户元素是否存在
		"""
		time.sleep(2)
		if self.login_handle.judge_account() != None:
			time.sleep(1.5)
			self.login_handle.click_account()
			time.sleep(2)
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		else:
			time.sleep(1.5)
			self.login_handle.manual_password_unlock()
			time.sleep(2)
			self.login_handle.click_account()
			time.sleep(1.5)
			self.login_out_app()
			time.sleep(2)
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

	

