#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from page.registration_page import RegistratonPage

class RegistrationHandle(object):
	def __init__(self,driver):
		self.driver = driver
		self.registration_page = RegistratonPage(self.driver)

	def judge_resgistration_title(self):
		"""
		判断是否是注册页面
		"""
		return self.registration_page.get_resgistration_title()

	def judge_validation_mobile(self):
		"""
		判断验证手机号码元素是否存在
		"""
		return self.registration_page.get_validation_mobile()

	def click_registration_cancel(self):
		"""
		点击右上角取消按钮
		"""
		self.registration_page.get_resgistration_cancel().click()

	def send_input_validation_mobile(self,mobile):
		"""
		输入手机号码
		"""
		self.registration_page.get_input_validation_mobile().send_keys(mobile)

	def clear_input_validation_mobile(self):
		"""
		清除输入框数据
		"""
		self.registration_page.get_input_validation_mobile().clear()


	def send_input_mobile_verification_code(self,code):
		"""
		输入短信验证码
		"""
		self.registration_page.get_input_mobile_verification_code().send_keys(code)

	def clear_input_mobile_verification_code(self):
		"""
		清除短信验证码
		"""
		self.registration_page.get_input_mobile_verification_code().clear()

	def click_sms_verification_code(self):
		"""
		点击获取短信验证码按钮
		"""
		self.registration_page.get_sms_verification_code().click()

	def click_agree_deal(self):
		"""
		点击勾选同意协议
		"""
		self.registration_page.get_agree_deal().click()

	def click_submit_validation(self):
		"""
		点击提交验证按钮
		"""
		self.registration_page.get_submit_validation().click()

	def judge_setting_password_text(self):
		"""
		判断设置密码元素是否存在
		"""
		return self.registration_page.get_setting_password_text()

	def send_setting_password_input(self,password):
		"""
		设置登录密码
		"""
		self.registration_page.get_setting_password_input().send_keys(password)

	def clear_setting_password_input(self):
		"""
		清除输入框内容
		"""
		self.registration_page.get_setting_password_input().clear()

	def send_recommended_id(self,recommendid):
		"""
		输入推荐人id
		"""
		self.registration_page.get_recommended_id().send_keys(recommendid)

	def click_commit_setting_succese(self):
		"""
		点击完成设置按钮
		"""
		self.registration_page.get_commit_setting_succese().click()

	def judge_resgistration_success(self):
		"""
		判断注册完成页面是否存在
		"""
		return self.registration_page.get_resgistration_success()


	def judge_resgistration_success_text(self):
		"""
		判断注册成功页面文案是否存在
		"""
		return self.registration_page.get_resgistration_success_text()

	def click_continue_real_name_authentication(self):
		"""
		点击继续实名认证
		"""
		self.registration_page.get_continue_real_name_authentication().click()

	def click_to_go_first(self):
		"""
		点击先逛一逛
		"""
		self.registration_page.get_to_go_first().click()

	def click_website_service_agreement(self):
		"""
		点击网站服务协议
		"""
		self.registration_page.get_website_service_agreement().click()

	def click_risk_note(self):
		"""
		点击风险提示书
		"""
		self.registration_page.get_risk_note().click()

	def click_registration_return(self):
		"""
		点击返回键，返回注册页面
		"""
		self.registration_page.get_registration_return().click()

