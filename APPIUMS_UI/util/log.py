#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
import logging
import time


class Logger(object):
	def __init__(self):
		self.logger = logging.getLogger()
		logging.root.setLevel(logging.NOTSET)
		self.log_file_name = "F:/APPIUMS_UI/log/Test.log"
		#日志输出级别
		self.console_output_level = "INFO"
		self.file_output_level = "DEBUG"
		#日志输出格式
		self.formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')

	def get_logger(self):
		"""封装logger"""
		if not self.logger.handlers:#避免重复日志
			console_handler = logging.StreamHandler()
			console_handler.setFormatter(self.formatter)
			console_handler.setLevel(self.console_output_level)
			self.logger.addHandler(console_handler)
			file_handler = logging.FileHandler(self.log_file_name)
			file_handler.setFormatter(self.formatter)
			file_handler.setLevel(self.file_output_level)
			self.logger.addHandler(file_handler)
			return self.logger

if __name__ == "__main__":
	Logger().get_logger().info(u'验证通过')