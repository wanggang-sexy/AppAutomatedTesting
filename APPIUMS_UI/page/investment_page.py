#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from util.get_by_local import GetByLocal
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver

class InvestmentPage(object):
	"""
	获取投资页面所有元素信息
	"""
	def __init__(self,driver):
		self.driver = driver
		self.get_by_local = GetByLocal(self.driver)


	def get_by_no(self):
		"""
		获取投资页面项目列表元素信息
		"""
		return self.get_by_local.get_element("investment_page_project_list_class","investment_page_element")
		

	def get_investment(self):
		"""
		获取投资tab页面元素
		"""
		return self.get_by_local.get_element("investment_page","investment_page_element")

if __name__ == "__main__":
	base = BaseDriver()
	driver = base.android_driver(0)
	abc = InvestmentPage(driver)
	print abc.get_investment()
	print abc.get_by_no()



		