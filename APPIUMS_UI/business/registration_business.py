#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from handle.registration_handle import RegistrationHandle
from handle.login_handle import LoginHandle
from util.get_linux import getcode
from base.swipe_page import SwipePage
from business.login_business import LoginBusiness
import time
import random


class RegistrationBusiness(object):
	def __init__(self,driver):
		self.driver = driver
		self.login_handle = LoginHandle(self.driver)
		self.registration_handle = RegistrationHandle(self.driver)
		self.swipe_page = SwipePage(self.driver)
		self.login_business = LoginBusiness(self.driver)

	def case_registration_001(self,i):#进入注册页面，元素存在
		self.login_handle.click_account()
		self.login_handle.click_free_registration()
		time.sleep(1)
		try:
			if self.registration_handle.judge_resgistration_title() != None:
				print u"注册页面元素存在"
				self.screenshots.screenshots(i)
				if self.registration_handle.judge_validation_mobile() != None:
					print u"验证手机号码元素存在"
					self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
				else:
					print u"验证手机号码元素不存在"
					self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
			else:
				print u"注册页面元素不存在"
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		except Exception,e:
			print u"用例失败:"+e


	def case_registration_002(self,i):#点击取消按钮，返回首页
		self.registration_handle.click_registration_cancel()
		time.sleep(1)
		try:
			if self.login_handle.judge_account() != None:
				print u"账户元素存在"
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
			else:
				print u"账户元素不存在"
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		except Exception,e:
			print u"用例失败:"+e

	def case_registration_003(self,i):#输入小于11位手机号码
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		time.sleep(1)
		try:
			if self.registration_handle.judge_resgistration_title() != None:
				print u"注册页面元素存在"
				self.registration_handle.send_input_validation_mobile("1891234561")
				self.registration_handle.click_sms_verification_code()
				time.sleep(5)
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
				time.sleep(2)
			else:
				print u"注册页面元素存在"
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		except Exception,e:
			print u"用例失败:"+e

	def case_registration_004(self,i):#输入大于11位手机号码
		self.registration_handle.send_input_validation_mobile("189456213412562")
		self.registration_handle.click_sms_verification_code()
		time.sleep(5)
		self.registration_handle.click_registration_cancel()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		time.sleep(2)


	def case_registration_005(self,i):#手机号码输入特殊字符
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		time.sleep(1)
		self.registration_handle.send_input_validation_mobile("@#!$%^&*,..;{}")
		self.registration_handle.click_sms_verification_code()
		time.sleep(5)
		self.registration_handle.click_registration_cancel()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		time.sleep(2)


	def case_registration_006(self,i):#输入11位手机号码，获取验证码成功
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		time.sleep(1)
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.click_sms_verification_code()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		time.sleep(5)
		self.registration_handle.click_registration_cancel()


	def case_registration_007(self,i):#同一账号，连续获取短信验证
		try:
			if self.login_handle.judge_account() != None:
				print u"账户元素存在"
				self.login_handle.click_account()
				time.sleep(1)
				self.login_handle.click_free_registration()
				self.registration_handle.send_input_validation_mobile("13945612300")
				self.registration_handle.click_sms_verification_code()
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
				time.sleep(5)
				self.registration_handle.click_registration_cancel()
				time.sleep(2)
				self.login_handle.click_account()
				time.sleep(1)
				self.login_handle.click_free_registration()
				self.registration_handle.send_input_validation_mobile("13945612300")
				self.registration_handle.click_sms_verification_code()
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
				time.sleep(5)
				self.registration_handle.click_registration_cancel()
				time.sleep(2)
				self.login_handle.click_account()
				time.sleep(1)
				self.login_handle.click_free_registration()
				self.registration_handle.send_input_validation_mobile("13945612300")
				self.registration_handle.click_sms_verification_code()
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
				time.sleep(5)
				self.registration_handle.click_registration_cancel()
				time.sleep(2)
				self.login_handle.click_account()
				time.sleep(1)
				self.login_handle.click_free_registration()
				self.registration_handle.send_input_validation_mobile("13945612300")
				self.registration_handle.click_sms_verification_code()
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
				time.sleep(5)
				self.registration_handle.click_registration_cancel()
			else:
				print u"账户元素不存在"
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		except Exception,e:
			print u"用例失败:"+e

	def case_registration_008(self,i):#重新获取短信验证码
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.click_sms_verification_code()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		time.sleep(40)
		self.registration_handle.click_sms_verification_code()
		time.sleep(40)
		self.registration_handle.click_sms_verification_code()
		time.sleep(40)
		self.registration_handle.click_sms_verification_code()
		time.sleep(0.5)
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		time.sleep(1)
		self.registration_handle.click_registration_cancel()

	def case_registration_009(self,i):#未获取短信验证码，输入内容，提交验证
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		time.sleep(1)
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.send_input_mobile_verification_code("000001")
		self.registration_handle.click_agree_deal()
		self.registration_handle.click_submit_validation()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.registration_handle.click_registration_cancel()

	def case_registration_010(self,i):#输入电话号码，点击提交验证
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.click_submit_validation()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

	def case_registration_011(self,i):#输入电话号码，输入错误的验证码，勾选协议，提交验证
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.send_input_mobile_verification_code("123456")
		self.registration_handle.click_agree_deal()
		self.registration_handle.click_submit_validation()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.registration_handle.click_registration_cancel()

	def case_registration_012(self,i):#输入手机号码和验证码，不勾选协议，提交验证
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.click_sms_verification_code()
		time.sleep(5)
		self.registration_handle.send_input_mobile_verification_code(getcode())
		self.registration_handle.click_submit_validation()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.registration_handle.click_registration_cancel()

	def case_registration_013(self,i):#输入短信验证码小于6位数
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.click_sms_verification_code()
		time.sleep(5)
		self.registration_handle.send_input_mobile_verification_code("1234")
		self.registration_handle.click_agree_deal()
		self.registration_handle.click_submit_validation()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.registration_handle.click_registration_cancel()

	def case_registration_014(self,i):#输入短信验证码大于6位
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.click_sms_verification_code()
		time.sleep(5)
		self.registration_handle.send_input_mobile_verification_code("123456789")
		self.registration_handle.click_agree_deal()
		self.registration_handle.click_submit_validation()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.registration_handle.click_registration_cancel()

	def case_registration_015(self,i):#输入已注册的账号
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		self.registration_handle.send_input_validation_mobile("13728628602")
		self.registration_handle.click_sms_verification_code()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		time.sleep(5)

	def case_registration_016(self,i):#查看网站服务协议页面
		time.sleep(1)
		self.registration_handle.click_website_service_agreement()
		time.sleep(5)
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.swipe_page.swipe_up()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.registration_handle.click_registration_return()
		time.sleep(1)

	def case_registration_017(self,i):#查看风险提示书
		time.sleep(1)
		self.registration_handle.click_risk_note()
		time.sleep(5)
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.swipe_page.swipe_up()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.swipe_page.swipe_up()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.swipe_page.swipe_up()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.registration_handle.click_registration_return()
		time.sleep(1)
		self.registration_handle.click_registration_cancel()

	def case_registration_018(self,i):#进入设置密码页面
		self.login_handle.click_account()
		time.sleep(1)
		self.login_handle.click_free_registration()
		time.sleep(1)
		mobilephone = str(random.randint(13728620000, 13728629999))
		self.registration_handle.send_input_validation_mobile(mobilephone)
		self.registration_handle.click_sms_verification_code()
		code = getcode()
		time.sleep(5)
		self.registration_handle.send_input_mobile_verification_code(code)
		self.registration_handle.click_agree_deal()
		self.registration_handle.click_submit_validation()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		try:
			if self.registration_handle.judge_setting_password_text() != None:
				print u"设置密码元素存在"
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
			else:
				print u"设置密码元素不存在"
				self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		except Exception,e:
			print u"用例失败:"+eseconds
		time.sleep(2)


	def case_registration_019(self,i):#进入设置页面，不输入任何内容，点击完成完成设置
		time.sleep(2)
		self.registration_handle.click_commit_setting_succese()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


	def case_registration_020(self,i):#设置小于5位数登录密码
		time.sleep(1)
		self.registration_handle.send_setting_password_input("s123")
		self.registration_handle.click_commit_setting_succese()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


	def case_registration_021(self,i):#设置登录密码是6位纯数字
		time.sleep(1)
		self.registration_handle.send_setting_password_input("123456")
		self.registration_handle.click_commit_setting_succese()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

	def case_registration_022(self,i):#设置登录密码是特殊字符
		time.sleep(1)
		self.registration_handle.send_setting_password_input("#$%@*&^()")
		self.registration_handle.click_commit_setting_succese()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

	'''
	def case_registration_023(self):#登录密码设置中文字符
		time.sleep(1)
		self.registration_handle.send_setting_password_input("未来的路酣畅")
		self.registration_handle.click_commit_setting_succese()
		self.driver.save_screenshot("../jpg/Test-"+str(time.time())+".png")
	'''

	def case_registration_024(self,i):#登录密码设置超过20个字符
		time.sleep(1)
		self.registration_handle.send_setting_password_input("qwioujiowbxmzcnbjhixz526894")
		self.registration_handle.click_commit_setting_succese()
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")


	def case_registration_025(self,i):#设置登录密码成功，跳入设置手势密码页面,设置手势密码
		time.sleep(1)
		self.registration_handle.clear_setting_password_input()
		time.sleep(1)
		self.registration_handle.send_setting_password_input("s123456")
		time.sleep(1)
		self.registration_handle.send_recommended_id("RCMAPX")
		time.sleep(2)
		self.registration_handle.click_commit_setting_succese()
		time.sleep(10)
		try:
			self.login_business.gesture_password()
		except Exception,e:
			print u"设置手势密码失败:"+e
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		else:
			print u"设置手势密码成功"
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

	def case_registration_026(self,i):#注册成功
		time.sleep(5)
		if self.registration_handle.judge_resgistration_success_text() != None:
			print u"注册成功！"
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		else:
			print u"注册失败！"
			self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

	def case_registration_027(self,i):#点击逛一逛按钮进入首页
		time.sleep(2)
		self.registration_handle.click_to_go_first()
		time.sleep(5)
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		time.sleep(2)
		self.login_handle.click_account()
		time.sleep(2)
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")

