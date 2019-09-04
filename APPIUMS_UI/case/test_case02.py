#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = "android"#设备类型
    desired_caps['platformVersion'] = "4.4.4"#系统版本号
    desired_caps['deviceName'] = "127.0.0.1:21503"#设备号
    #desired_caps['App'] = "F:\heshidaiapppakage\hsdjr_v2.10.apk"#APP路径
    desired_caps['appPackage'] = "com.heshidai.app"#应用包名
    desired_caps['appActivity'] = "com.heshidai.app.activity.finance.WelcomeActivity"#应用的activity
    desired_caps['unicodeKeyboard'] = 'True'#Unicode类型
    desired_caps['resetKeyboard'] = 'True'#不显示键盘
    driver = webdriver.Remote('http://localhost:4700/wd/hub', desired_caps)
    time.sleep(10)
    return driver


def get_unlock_value():
        time.sleep(2)
        lock_pattern = driver.find_element_by_id('com.heshidai.app:id/lock_setup_pattern')
        x = lock_pattern.location.get('x')
        y = lock_pattern.location.get('y')
        width = lock_pattern.size.get('width')
        height = lock_pattern.size.get('height')
        print(x, y, width, height)
        offset = width / 6 
        p11 = int(x + width / 6), int(y + height / 6)#第一个点
        p12 = int(x + width / 2), int(y + height / 6)#第二个点
        p13 = int(x + width - offset), int(y + height / 6)#第三个点
        p21 = int(x + width / 6), int(y + height / 2)#第四个点
        p22 = int(x + width / 2), int(y + height / 2)#第五个点
        p23 = int(x + width - offset), int(y + height / 2)#第六个点
        p31 = int(x + width / 6), int(y + height - offset)#第七个点
        p32 = int(x + width / 2), int(y + height - offset)#第八个点
        p33 = int(x + width - offset), int(y + height - offset)#第九个点
        p2 = p12[0] - p11[0]#偏移量
        p3 = p13[0] - p12[0]#偏移量
        return p11,p2,p3

def move_to():
    data = get_unlock_value()
    time.sleep(2)
    if driver.find_element_by_name('设置新手势密码') != None:
        TouchAction(driver).press(x=data[0][0], y=data[0][1]).move_to(x=data[1], y=0).wait(1000).move_to(x=data[2], y=0).wait(1000).move_to(x=0, y=data[1]).wait(1000).move_to(x=0, y=data[2]).wait(1000).release().perform()
        if driver.find_element_by_name('确认新手势密码') !=None:
            TouchAction(driver).press(x=data[0][0], y=data[0][1]).move_to(x=data[1], y=0).wait(1000).move_to(x=data[2], y=0).wait(1000).move_to(x=0, y=data[1]).wait(1000).move_to(x=0, y=data[2]).wait(1000).release().perform()
        else:
            print '确认手势密码错误'
    else:
        TouchAction(driver).press(x=data[0][0], y=data[0][1]).move_to(x=data[1], y=0).wait(1000).move_to(x=data[2], y=0).wait(1000).move_to(x=0, y=data[1]).wait(1000).move_to(x=0, y=data[2]).wait(1000).release().perform()
        print "设置手势密码元素不存在"

def get_login():
    driver.find_element_by_name('账户').click()
    driver.find_element_by_id("com.heshidai.app:id/et_login_tel").send_keys("18928480059")
    driver.find_element_by_id("com.heshidai.app:id/et_login_tel_psd").send_keys("wang1234")
    driver.find_element_by_id('com.heshidai.app:id/login_now').click()

driver = get_driver()
#get_login()
#move_to()
time.sleep(5)
data = get_unlock_value()
TouchAction(driver).press(x=data[0][0], y=data[0][1]).move_to(x=data[1], y=0).wait(1000).move_to(x=data[2], y=0).wait(1000).move_to(x=0, y=data[1]).wait(1000).move_to(x=0, y=data[2]).wait(1000).release().perform()
