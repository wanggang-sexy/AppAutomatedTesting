# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
import os
from util.write_user_command import WriteUserCommand

class DelFolder(object):
	def __init__(self):
		self.write_user_file = WriteUserCommand()
	def del_folder(self,path=None):
		if path == None:
			path='F:/APPIUMS_UI/jpg'
			folder = os.listdir(path)#文件夹
			if len(folder)>0:
				print u'= = = = = 开始删除目录 = = = = = '
				for i in range(len(folder)):
					os.rmdir('F:/APPIUMS_UI/jpg/'+str(i))
				print u'= = = = = 已删除目录 = = = = ='
			else:
				print u'= = = = = 不做删除动作 = = = = ='
		else:
			folder = os.listdir(path)#文件夹
			if len(folder)>0:
				print u'= = = = = 开始删除目录 = = = = = '
				for i in range(len(folder)):
					os.rmdir('F:/APPIUMS_UI/jpg/'+str(i))
				print u'= = = = = 已删除目录 = = = = ='
			else:
				print u'= = = = = 不做删除动作 = = = = = '

	def create_folder(self,path=None):
		line = self.write_user_file.get_file_lines()
		if path == None:
			path='F:/APPIUMS_UI/jpg'
			folder = os.listdir(path)#文件夹
			if line >0 and len(folder)<=0:
				print '= = = = = 开始创建目录 = = = = ='
				for i in range(line):
					os.makedirs('F:/APPIUMS_UI/jpg/'+str(i))
				print '= = = = = 目录创建完成 = = = = ='
			else:
				print '= = = = = 不创建目录 = = = = ='
		else:
			folder = os.listdir(path)#文件夹
			print len(folder)
			if line >0 and len(folder)<=0:
				print '= = = = = 开始创建目录 = = = = ='
				for i in range(line):
					os.makedirs('F:/APPIUMS_UI/jpg/'+str(i))
				print '= = = = = 目录创建完成 = = = = ='
			else:
				print '= = = = = 不创建目录 = = = = ='

	def del_is_jpg(self,path=None):
		if path == None:
			path = 'F:/APPIUMS_UI/jpg'
			lists = os.listdir(path)
			if len(lists)>0:
				for i in lists:
					os.remove(path+'/'+i)
				print "= = = = = 图片已全部删除 = = = = ="
			else:
				print "= = = = = 无数据内容，不做删除动作 = = = = ="
		else:
			lists = os.listdir(path)
			if len(lists)>0:
				for i in lists:
					os.remove(path+'/'+i)
				print "= = = = = 图片已全部删除 = = = = ="
			else:
				print "= = = = = 无数据内容，不做删除动作 = = = = ="



		


if __name__ == '__main__':
	#dels = DelFolder()
	#dels.del_folder()
	#dels.create_folder()
	#dels.del_is_jpg()
	for j in xrange(1,11):
		print j
	for j in xrange(1,11):
		print j