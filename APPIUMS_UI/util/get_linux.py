#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')

import paramiko
def getcode():
	#获取注册短信验证码,从日志后台读取短信验证码
	lists = []
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect('192.168.254.52', 22, username='root', password='hsd123', timeout=4)
	stdin, stdout, stderr  = client.exec_command('cat /usr/local/tomcat7-8084/logs/catalina.out')
	result = stdout.readlines()
	#file = open("F:/APPIUMS_UI/log/test.txt","w")
	#file.write(result[-10:-1])
	for i in result[-10:-1]:
		lists.append(i.split("[HSD-MOBILE]")[-1])
	lists = lists[-2].split(":")[-2:-1]
	return int(lists[0].split(",")[0][1:7])

	client.close()

if __name__ == "__main__":
	print getcode()


