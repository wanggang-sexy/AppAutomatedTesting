#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from page.investment_page import InvestmentPage
from base.base_driver import BaseDriver
class InvestmentHandle(object):
	"""
	操作投资页面元素
	"""
	def __init__(self,driver):
		self.driver = driver
		self.investment_page = InvestmentPage(self.driver)


	def click_project_list1(self,n):
		"""
		点击项目列表中第n个项目
		"""
		elements = self.investment_page.get_by_no()
		elements[n].click()
		

	def click_investment_tab(self):
		"""
		点击投资投资tab
		"""
		self.investment_page.get_investment().click()




if __name__ == "__main__":
	base = BaseDriver()
	driver = base.android_driver(0)
	handle = InvestmentHandle(driver)
	print handle.click_investment_tab()
	print handle.click_project_list1(1)


