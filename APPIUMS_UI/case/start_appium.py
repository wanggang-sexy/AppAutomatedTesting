#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from keyword import iskeyword as _iskeyword
from util.get_linux import getcode
from business.login_business import LoginBusiness
def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = "android"#设备类型
    desired_caps['platformVersion'] = "4.4.2"#系统版本号
    desired_caps['deviceName'] = "127.0.0.1:21533"#设备号
    #desired_caps['automationName'] = "UiAutomator2"
    desired_caps['App'] = "F:\\APPIUMS_UI\\apps\\heshidai.apk"#APP路径
    desired_caps['appPackage'] = "com.heshidai.app"#应用包名
    desired_caps['appActivity'] = "com.heshidai.app.activity.finance.WelcomeActivity"#com.heshidai.app.activity.finance.WelcomeActivity"#应用的activity
    desired_caps['unicodeKeyboard'] = "True"#Unicode类型
    desired_caps['resetKeyboard'] = "True"#不显示键盘
    #desired_caps['noReset'] = "true"#不会重复安装APP
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    return driver



def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height


    #向左边滑动
def swipe_left():
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10
    driver.swipe(x1,y1,x,y1)



#向右边滑动
def swipe_right():
	#[100,200]
	x1 = get_size()[0]/10
	y1 = get_size()[1]/2
	x = get_size()[0]/10*9
	driver.swipe(x1,y1,x,y1,2000)

#向上滑动
def swipe_up():
	#[100,200]direction
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10*9
	y = get_size()[1]/10
	driver.swipe(x1,y1,x1,y,1000)

#向下滑动
def swipe_down():
	#[100,200]
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10
	y = get_size()[1]/10*9
	driver.swipe(x1,y1,x1,y)

def swipe_on(direction):
	if direction == 'up':
		swipe_up()
	elif direction == 'down':
		swipe_down()
	elif direction == 'left':
		swipe_left()
	else:
		swipe_right()




def go_login(driver):
    get_local_by = GetByLocal(driver)
    get_local_by.get_element('account').click()
    get_local_by.get_element('mobile_login').send_keys('18928480059')
    get_local_by.get_element('mobile_login_password').send_keys('wanggang093431')
    get_local_by.get_element('login_buttion').click()



driver = get_driver()

try:
    driver.find_element_by_name("账户") != None
    
except Exception as result:
    print "未知错误 %s" % result
else:
    driver.find_element_by_name("账户").click()
    driver.find_element_by_name("免费注册").click()

finally:
    print("执行完成，但是不保证正确")


driver.find_element_by_id("com.heshidai.app:id/et_regist_phonenum").send_keys("13728628698")
driver.find_element_by_id("com.heshidai.app:id/bt_regist_getmsgcode").click()


driver.find_element_by_id("com.heshidai.app:id/et_regist_writecode").send_keys(getcode())
time.sleep(2)

driver.find_element_by_id("com.heshidai.app:id/tv_regist_model_start").click()

driver.find_element_by_id("com.heshidai.app:id/regist_commit_msgcode").click()

driver.find_element_by_id("com.heshidai.app:id/et_regist_passwd").send_keys("s123456")

driver.find_element_by_id("com.heshidai.app:id/regist_commit_succ").click()

login_buess = LoginBusiness(driver)
login_buess.gesture_password()

time.sleep(10)

driver.close_app()









'''
time.sleep(2)
driver.find_element_by_id("com.heshidai.app:id/et_regist_phonenum").send_keys("13728628633")
time.sleep(2)
driver.find_element_by_id("com.heshidai.app:id/bt_regist_getmsgcode").click()
time.sleep(2)
driver.find_element_by_id("com.heshidai.app:id/tv_regist_model").click()
'''

'''
driver.find_element_by_id("com.heshidai.app:id/et_regist_writecode").send_keys(getcode())
time.sleep(5)

driver.find_element_by_id("com.heshidai.app:id/tv_regist_model_start").click()

time.sleep(2)

driver.find_element_by_id("com.heshidai.app:id/regist_commit_msgcode").click()
'''

'''
swipe_up()
elements = driver.find_element_by_id("com.heshidai.app:id/ll_home_footview_save")

elements.click()

time.sleep(3)
#el = driver.find_element_by_class_name("android.widget.ListView")

if driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'信息披露')]") != None:
    print u"存在"

else:
    print u"不存在"
#获取当前页面所有的contexts
webview = driver.contexts
#获取到的contexts list里面去挨个循环
for context in webview:
    #判断循环中的单个context是否是webview，如果是就进行切换，并跳出循环
    if "WEBVIEW" in context:
        driver.switch_to.context(context)
        break
driver.find_element_by_link_text("关于我们").click()
time.sleep(3)
#获取当前页面所有的contexts
webview = driver.contexts
#获取到的contexts list里面去挨个循环
for context in webview:
    #判断循环中的单个context是否是webview，如果是就进行切换，并跳出循环
    if "NATIVE" in context:
        driver.switch_to.context(context)
        break
driver.find_element_by_id("com.heshidai.app:id/title_left_iv").click()
'''

'''
driver.press_keycode(7)

if driver.find_element_by_id("com.heshidai.app:id/bannerViewPager") != None:
    print u"banner元素存在"
    driver.find_element_by_id("com.heshidai.app:id/bannerViewPager").click()
    time.sleep(5)
    title = driver.find_element_by_id("com.heshidai.app:id/title_middle_tv") 
    if title != None:
        print title.get_attribute("text")
        time.sleep(2)
        swipe_up()
        time.sleep(1)
        swipe_up()
        time.sleep(1)
        swipe_up()
        time.sleep(1)
        swipe_up()
        time.sleep(1)

    else:
        print u"title不存在"
else:
    print u"banner元素不存在"
'''

'''
time.sleep(5)
driver.find_element_by_name('账户').click()

print driver.find_element_by_class_name("android.widget.TextView").get_attribute("text")


element = driver.find_element_by_id('com.heshidai.app:id/account_menu')
elements = element.find_elements_by_id('com.heshidai.app:id/menu_item_text')
#elements = element.find_elements_by_class_name('android.widget.RelativeLayout')
for i in elements:
    print i.get_attribute("text")
elements[1].click()

'''

'''
driver.find_element_by_android_uiautomator('new UiSelector().text("投资")').click()
driver.find_element_by_name('投资').click()

element = driver.find_element_by_id('com.heshidai.app:id/invest_lv')
elements = element.find_elements_by_class_name('android.widget.RelativeLayout')
ele = elements[1].get_attribute("name")
eles = elements[1].text
time.sleep(5)
elements[1].click()
'''