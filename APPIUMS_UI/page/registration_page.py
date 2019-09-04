#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from util.get_by_local import GetByLocal
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistratonPage(object):
	def __init__(self,driver):
		self.driver = driver
		self.get_by_local = GetByLocal(self.driver)

	def get_resgistration_title(self):
		"""
		获取注册页面title
		"""
		return self.get_by_local.get_element("resgistration_title","registration_element")

	def get_resgistration_cancel(self):
		"""
		获取右上角取消按钮
		"""
		return self.get_by_local.get_element("registration_cancel","registration_element")

	def get_validation_mobile(self):
		"""
		获取验证手机号元素
		"""
		return self.get_by_local.get_element("validation_mobile","registration_element")

	def get_input_validation_mobile(self):
		"""
		获取输入手机号码框元素
		"""
		return self.get_by_local.get_element("input_validation_mobile","registration_element")

	def get_input_mobile_verification_code(self):
		"""
		获取验证码输入框元素
		"""
		return self.get_by_local.get_element("input_mobile_verification_code","registration_element")

	def get_sms_verification_code(self):
		"""
		获取短信验证码按钮元素
		"""
		return self.get_by_local.get_element("sms_verification_code","registration_element")

	def get_agree_deal(self):
		"""
		获取勾选协议元素
		"""
		return self.get_by_local.get_element("agree_deal","registration_element")

	def get_submit_validation(self):
		"""
		获取提交验证码按钮
		"""
		return self.get_by_local.get_element("submit_validation","registration_element")

	def get_setting_password_text(self):
		"""
		获取设置密码文案元素
		"""
		return self.get_by_local.get_element("setting_password_text","registration_element")

	def get_setting_password_input(self):
		"""
		获取登录密码输入框元素
		"""
		return self.get_by_local.get_element("setting_password_input","registration_element")

	def get_recommended_id(self):
		"""
		获取推荐人id元素
		"""
		return self.get_by_local.get_element("recommended_id","registration_element")

	def get_commit_setting_succese(self):
		"""
		获取完成设置按钮元素
		"""
		return self.get_by_local.get_element("commit_setting_succese","registration_element")

	def get_resgistration_success(self):
		"""
		获取注册完成元素
		"""
		return self.get_by_local.get_element("resgistration_success","registration_element")

	def get_resgistration_success_text(self):
		"""
		获取注册完成文案元素
		"""
		return self.get_by_local.get_element("resgistration_success_text","registration_element")

	def get_continue_real_name_authentication(self):
		"""
		获取继续完成实名认证元素
		"""
		return self.get_by_local.get_element("continue_real_name_authentication","registration_element")

	def get_to_go_first(self):
		"""
		获取先逛一逛元素
		"""
		return self.get_by_local.get_element("to_go_first","registration_element")

	def get_website_service_agreement(self):
		"""
		获取网站服务协议元素
		"""
		return self.get_by_local.get_element("website_service_agreement","registration_element")

	def get_risk_note(self):
		"""
		获取风险提示书
		"""
		return self.get_by_local.get_element("risk_note","registration_element")

	def get_registration_return(self):
		"""
		获取返回元素
		"""
		return self.get_by_local.get_element("registration_return","registration_element")

