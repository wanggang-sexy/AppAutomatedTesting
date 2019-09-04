#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand
class BaseDriver(object):
    def __init__(self):
        self.write_file = WriteUserCommand()

    def android_driver(self,i):
        print "this is android_driver:",i
        platformVersion = self.write_file.get_value("user_info_"+str(i),'platformVersion')
        deviceName = self.write_file.get_value("user_info_"+str(i),'deviceName')
        port = self.write_file.get_value("user_info_"+str(i),'port')    
        desired_caps = {}
        desired_caps['platformName'] = "android"#设备类型
        #desired_caps['automationName'] = "UiAutomator2"#toast提示
        desired_caps['platformVersion'] = platformVersion#系统版本号
        desired_caps['deviceName'] = deviceName#设备号
        desired_caps['App'] = "F:/heshidaiapppakage/heshidai.apk"#APP路径
        desired_caps['appPackage'] = "com.heshidai.app"#应用包名
        desired_caps['appActivity'] = "com.heshidai.app.activity.finance.WelcomeActivity"#应用的activity
        desired_caps['unicodeKeyboard'] = "True"#Unicode类型
        desired_caps['resetKeyboard'] = "True"#不显示键盘
        #desired_caps['noReset'] = "true"#不会重复安装APP
        self.driver = webdriver.Remote('http://localhost:'+port+'/wd/hub', desired_caps)
        time.sleep(20)
        return self.driver
    def ios_driver(self):
        pass
    def get_driver(self):
        pass
        

if __name__ == "__main__":
    basedriver = BaseDriver()
    print basedriver.android_driver('0')