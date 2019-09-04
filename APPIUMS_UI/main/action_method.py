#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
import time
from base.base_driver import BaseDriver
from business.login_business import LoginBusiness
from business.account_business import AccountBusiness
from business.registration_business import RegistrationBusiness
from util.log import Logger
from base.closes_app import ClosesApp


class ActionMethod(object):
	def __init__(self,i):
		base_driver = BaseDriver()
		self.driver = base_driver.android_driver(i)
		self.login_business = LoginBusiness(self.driver)
		self.account_business = AccountBusiness(self.driver)
		self.registration_business = RegistrationBusiness(self.driver)
		self.closes_app = ClosesApp(self.driver)

	def kill_App(self):
		self.closes_app.closes_quites()

	
	def action_login_001(self,i):

		'''判断启动页面的轮播元素是都存在'''
		try:
			self.login_business.login_judge01(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"
	def action_login_002(self,i):
		''' 判断账户元素是否存在'''
		try:
			self.account_business.account_page_account(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"
	def action_login_003(self,i):
		'''进入登录页面判断元素是否存在'''
		try:
			self.login_business.login_judge02(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"
	def action_login_004(self,i):
		'''未输入内容，点击登录按钮'''

		try:
			self.login_business.login_err01(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_005(self,i):
		'''输入账号，点击登录按钮'''
		try:
			self.login_business.login_err02(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_006(self,i):
		'''输入密码点击登录按钮'''

		try:
			self.login_business.login_err03(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_007(self,i):
		'''密码错误,点击登录'''

		try:
			self.login_business.login_err04(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_008(self,i):
		'''账号错误'''

		try:
			self.login_business.login_err05(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_009(self,i):
		'''账户或密码错误5次，锁定账户'''

		try:
			self.login_business.login_err06(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_010(self,i):
		'''输入无效账号密码登录'''

		try:
			self.login_business.login_err07(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_011(self,i):
		'''登录成功,设置手势密码'''

		try:
			self.login_business.login_pass01(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"
	def action_login_012(self,i):
		'''判断弹窗，是否存在'''

		try:
			self.login_business.judge_bounced(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_013(self,i):
		'''我的账户元素是否存在'''

		try:
			self.account_business.my_account(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_014(self,i):
		'''杀掉APP进程，再次启动APP'''

		try:
			self.login_business.close_start_app(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_015(self):
		'''手势密码解锁'''

		try:
			self.login_business.manual_password_unlock()
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_016(self,i):
		'''判断弹窗，是否存在'''
		try:
			self.login_business.judge_bounced(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_017(self):
		'''点击账户'''
		try:
			self.login_business.click_click_account()
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_018(self,i):
		'''退出APP登录'''

		try:
			self.account_business.login_out_app(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"
		
	def action_login_019(self,i):
		'''切换普通登录'''
		try:
			self.login_business.login_normal(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"
	def action_login_020(self,i):
		'''未输入内容，进入普通用户登录'''

		try:
			self.login_business.normal_err01(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_021(self,i):
		'''输入账号，普通登录'''
		try:
			self.login_business.normal_err02(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_022(self,i):
		'''输入密码，普通登录'''
		try:
			self.login_business.normal_err03(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_023(self,i):
		'''密码错误，普通登录'''

		try:
			self.login_business.normal_err04(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_024(self,i):
		'''账号错误，普通登录'''
		try:
			self.login_business.normal_err05(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_025(self,i):
		'''账号或密码错误5次，账户锁定'''

		try:
			self.login_business.normal_err06(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_026(self,i):
		'''无效账户，普通登录'''

		try:
			self.login_business.normal_err07(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"


	def action_login_027(self,i):
		'''普通登录成功，设置手势密码'''
		try:
			self.login_business.normal_pass01(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_028(self,i):
		'''判断弹窗，是否存在'''

		try:
			self.login_business.judge_bounced(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_029(self,i):
		'''我的账户元素是否存在'''

		try:
			self.account_business.my_account(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_030(self,i):
		'''杀掉APP进程，再次启动APP'''

		try:
			self.login_business.close_start_app(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_031(self):
		'''手势密码解锁'''

		try:
			self.login_business.manual_password_unlock()
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_032(self,i):
		'''判断弹窗，是否存在'''

		try:
			self.login_business.judge_bounced(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_033(self):
		'''点击账户'''

		try:
			self.login_business.click_click_account()
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_034(self,i):
		'''退出APP登录'''

		try:
			self.account_business.login_out_app(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def action_login_035(self,i):
		'''从登录页面返回首页'''
		try:
			self.login_business.login_err08(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"


	def action_login_036(self,i):
		'''输入手机号码，点击取消返回首页'''
		try:
			self.login_business.login_err09(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"


	def action_login_037(self,i):
		'''输入密码，点击取消返回首页'''
		try:
			self.login_business.login_err10(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"



	def action_login_038(self,i):
		'''输入手机号码和密码，点击取消返回首页'''
		try:
			self.login_business.login_err11(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"


	def action_login_039(self,i):
		'''输入手机和密码，切后台，5s，启动APP，数据存在'''
		try:
			self.login_business.login_err12(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"



	def action_login_040(self,i):
		'''输入手机和密码，杀掉进程，启动，数据不存在'''
		try:
			self.login_business.login_err13(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"



	def action_login_041(self,i):
		'''普通登录返回首页'''
		try:
			self.login_business.normal_err08(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"



	def action_login_042(self,i):
		'''输入用户名，返回首页'''
		try:
			self.login_business.normal_err09(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"




	def action_login_043(self,i):
		'''输入密码，返回首页'''
		try:	
			self.login_business.normal_err10(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"



	def action_login_044(self,i):
		'''输入用户名和密码，返回首页'''
		try:
			self.login_business.normal_err11(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"



	def action_login_045(self,i):
		'''输入用户名和密码,切后台，等待5s，在启动，数据存在'''
		try:
			self.login_business.normal_err12(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"



	def action_login_046(self,i):
		'''输入用户名和密码，杀掉进程，在启动，数据不存在，默认显示登录页面'''
		try:	
			self.login_business.normal_err13(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"
		
		
	def registration_case_001(self,i):
		'''进入注册页面，元素存在'''
		try:
			self.registration_business.case_registration_001(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_002(self,i):
		'''点击取消按钮，返回首页'''
		try:
			self.registration_business.case_registration_002(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"	

	def registration_case_003(self,i):
		'''输入小于11位手机号码'''
		try:
			self.registration_business.case_registration_003(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_004(self,i):
		'''输入大于11位手机号码'''
		try:
			self.registration_business.case_registration_004(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_005(self,i):
		'''手机号码输入特殊字符'''
		try:
			self.registration_business.case_registration_005(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_006(self,i):
		'''输入11位手机号码，获取验证码成功'''
		try:
			self.registration_business.case_registration_006(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_007(self,i):
		'''同一账号，连续获取短信验证'''
		try:
			self.registration_business.case_registration_007(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_008(self,i):
		'''重新获取短信验证码'''
		try:
			self.registration_business.case_registration_008(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_009(self,i):
		'''未获取短信验证码，输入内容，提交验证'''
		try:
			self.registration_business.case_registration_009(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_010(self,i):
		'''输入电话号码，点击提交验证'''
		try:
			self.registration_business.case_registration_010(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_011(self,i):
		'''输入电话号码，输入错误的验证码，勾选协议，提交验证'''
		try:
			self.registration_business.case_registration_011(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_012(self,i):
		'''输入手机号码和验证码，不勾选协议，提交验证'''
		try:
			self.registration_business.case_registration_012(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_013(self,i):
		'''输入短信验证码小于6位数'''
		try:
			self.registration_business.case_registration_013(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_014(self,i):
		'''输入短信验证码大于6位'''
		try:
			self.registration_business.case_registration_014(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_015(self,i):
		'''输入已注册的账号'''
		try:
			self.registration_business.case_registration_015(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_016(self,i):
		'''查看网站服务协议页面'''
		try:
			self.registration_business.case_registration_016(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_017(self,i):
		'''查看风险提示书'''
		try:
			self.registration_business.case_registration_017(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_018(self,i):
		'''进入设置密码页面'''
		try:		
			self.registration_business.case_registration_018(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_019(self,i):
		'''进入设置页面，不输入任何内容，点击完成完成设置'''
		try:
			self.registration_business.case_registration_019(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_020(self,i):
		'''设置小于5位数登录密码'''
		try:
			self.registration_business.case_registration_020(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_021(self,i):
		'''设置登录密码是6位纯数字'''
		try:
			self.registration_business.case_registration_021(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_022(self,i):
		'''设置登录密码是特殊字符'''
		try:
			self.registration_business.case_registration_022(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_023(self):
		'''
		无效用例
		try:
			self.registration_business.case_registration_023()

		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"
		'''

	def registration_case_024(self,i):
		'''登录密码设置超过20个字符'''
		try:
			self.registration_business.case_registration_024(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_025(self,i):
		'''设置登录密码成功，跳入设置手势密码页面,设置手势密码'''
		try:
			self.registration_business.case_registration_025(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_026(self,i):
		'''注册成功'''
		try:
			self.registration_business.case_registration_026(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_027(self,i):
		'''点击逛一逛按钮进入首页'''
		try:
			self.registration_business.case_registration_027(i)
		except Exception,e:
			print u"用例失败:"+e
		else:
			print u"用例执行成功"

	def registration_case_028(self,i):
		'''退出APP'''
		try:
			self.account_business.login_out_app(i)
		except Exception,e:
			print u"退出APP失败:"+e
		else:
			print u"退出APP成功"



		




