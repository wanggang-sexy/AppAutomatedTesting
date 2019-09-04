# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')

class ScreenShots(object):
	def __init__(self,driver):
		self.driver = driver
	def screenshots(self,i):
		#self.driver.save_screenshot("../jpg/"+str(i)+"Test-"+str(time.time())+".png")
		self.driver.get_screenshot_as_file("../jpg/"+str(i)+"Test-"+str(time.time())+".png")