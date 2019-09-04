import sys
sys.path.append('F:/APPIUMS_UI')


class ClosesApp(object):
	def __init__(self,driver):
		self.driver = driver

	def closes_quites(self):
		self.driver.quit()


