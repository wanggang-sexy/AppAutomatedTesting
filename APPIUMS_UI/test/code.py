# -*- coding: utf-8 -*-

from selenium import webdriver
import time

def click_number1(i):
    n=1
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="showdownlist"]/ul/li['+str(i)+']/span[1]/a').click()
    print driver.current_window_handle # 输出当前窗口句柄
    handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
        

    for handle in handles:# 切换窗口（切换到搜狗）
        if handle!=driver.current_window_handle:
            #print 'switch to ',handle
            driver.switch_to_window(handle)
            #print driver.current_window_handle # 输出当前窗口句柄（搜狗）
            break
    for i in range(101):
        time.sleep(5)
        # 刷新页面
        driver.refresh()
        print 'ok'+u'第'+str(n)+u'次'
        n=n+1

    driver.close() #关闭当前窗口（搜狗）
    driver.switch_to_window(handles[0]) #切换回窗口
    time.sleep(10)


def click_number2(i):
    n=1
    driver.find_element_by_id('dynamic').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="showdownlist"]/ul/li['+str(i)+']/span[1]/a').click()
    print driver.current_window_handle # 输出当前窗口句柄
    handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
        

    for handle in handles:# 切换窗口（切换到搜狗）
        if handle!=driver.current_window_handle:
            #print 'switch to ',handle
            driver.switch_to_window(handle)
            #print driver.current_window_handle # 输出当前窗口句柄（搜狗）
            break
    for i in range(101):
        time.sleep(5)
        # 刷新页面
        driver.refresh()
        print 'ok'+u'第'+str(n)+u'次'
        n=n+1
    driver.close() #关闭当前窗口（搜狗）
    driver.switch_to_window(handles[0]) #切换回窗口
    time.sleep(10)

def click_number3(i):
    n=1
    driver.find_element_by_id('info-center').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="showdownlist"]/ul/li['+str(i)+']/span[1]/a').click()
    print driver.current_window_handle # 输出当前窗口句柄
    handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）

    for handle in handles:# 切换窗口（切换到搜狗）
        if handle!=driver.current_window_handle:
            #print 'switch to ',handle
            driver.switch_to_window(handle)
            #print driver.current_window_handle # 输出当前窗口句柄（搜狗）
            break
    for i in range(101):
        time.sleep(5)
        # 刷新页面
        driver.refresh()
        print 'ok'+u'第'+str(n)+u'次'
        n=n+1
    driver.close() #关闭当前窗口（搜狗）
    driver.switch_to_window(handles[0]) #切换回窗口
    time.sleep(10)

def click_number4(i):
    n=1
    driver.find_element_by_id('mediareport').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="showdownlist"]/div['+str(i)+']/div/h1/a').click()
    print driver.current_window_handle # 输出当前窗口句柄
    handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）

    for handle in handles:# 切换窗口（切换到搜狗）
        if handle!=driver.current_window_handle:
            #print 'switch to ',handle
            driver.switch_to_window(handle)
            #print driver.current_window_handle # 输出当前窗口句柄（搜狗）
            break
    for i in range(101):
        time.sleep(5)
        # 刷新页面
        driver.refresh()
        print 'ok'+u'第'+str(n)+u'次'
        n=n+1
    driver.close() #关闭当前窗口（搜狗）
    driver.switch_to_window(handles[0]) #切换回窗口
    time.sleep(10)

if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.get("http://192.168.254.104:8300/SF/webnotice.html")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.implicitly_wait(10)
    #for j in xrange(1,11):
    #    click_number1(j)
    #for j in xrange(1,11):
    #    click_number2(j)
    for j in xrange(1,11):
        click_number3(j)
    for j in xrange(1,11):
        click_number4(j)



'''
# 添加Cookie
driver.add_cookie({'name':'BAIDUID','value':'7C451D65B715E998E6CD4BF1B9715707:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'JCOUp4TmEwdEI1LTVSY05wc29jbTV4bHF0bjBuNXVzTUFlbUZsQlhafkJUQnBiQVFBQUFBJCQAAAAAAAAAAAEAAADBpR5vAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMG~8lrBv~JaUl'})
'''
'''
n=1
for i in range(100):
    time.sleep(5)
# 刷新页面
    driver.refresh()

    print 'ok'+u'第'+n+u'次'
    n=n+1

# 获取登录用户名并打印


#关闭浏览器
'''

'''
import requests
import json



def borrowlist(basepath):
    url = basepath+'/borrow/syncBorrowInfo.html'
    bo={
        "annualRate":'10.00',
        "auditOpinion":'111',
        "auditStep":'1',
        "borrowAmount":'150000',
        "borrowUserType": '0',
        "borrowWay":'1',
        "danType": '1',
        "deadLine":'3',
        "detail":"asd",
        "guaranteeId":'3',
        "increaseRate":'2.50',
        "isDayThe": '2',
        "paymentMode": '3',
        "purpose": '1',
        "realBorrowerName": '111',
        "userId": '63657268'
        }
    borrowlist=[]
    borrowlist["borrowInfo"]=bo
    borrowlist["sign"]="0000"
    print borrowlist
    r = requests.post(url, data=borrowlist)
    print r.text

if __name__ == "__mian__":
    bankbasepath="http://183.62.205.226:8333/SF"
    borrowlist(bankbasepath)

'''



#import json

#print xrange(3,5)[1]


#dicts={'a':'aa','b':['{"c":"cc","d":"dd"}',{"f":{"e":"ee"}}]}
#dicke={}

#key1=dicts['a']
#key2=dicts['b']

#key3=key2[0]
#key4=key2[1]
#dicke['a']=key1
#key5=key4['f']

#print dict(dicke.items() + key5.items() + json.loads(key3).items())


#def numebr(n):
#    if n == 0:
#        return 1
 #   else:
#      return n * numebr(n-1)
#print numebr(3)



'''
#通讯录
print('''#|---欢迎进入通讯录---|
#|---1、查询联系人信息---|
#|---2、插入新的联系人---|
#|---3、删除联系人信息---|
#|---4、退出通讯录程序---|
''')
addressBook = {'小杨':12345678,'小张':12345679,'小赵':12345670}
while 1:
    order_code =raw_input('请输入指令代码：')
    if order_code.isdigit() == False:    #判断指令是否只有数字组成
        print('您输入的指令代码格式错误，请按照提示重新输入！')
        continue
    item = int(order_code)    #将输入指令转换为整型

    if item == 4:
        print('感谢使用通讯录！')
        break      #结束循环
    #输入联系人姓名
    name = raw_input('请输入联系人姓名：')
    if item == 1:      #查询联系人信息
        if name in addressBook:
            print(name,':',addressBook[name])
            continue     #结束当前循环
        else:
            print('联系人不存在。')
    if item == 2:     #新建联系人
        if name in addressBook:
            print('你输入的联系人在通讯录中已经存在--->>',name,':',addressBook[name])
            is_Edit = raw_input('是否需要修改联系人的信息：(Y/N)')    #判断是否需要修改当前联系人信息
            if is_Edit == 'Y':
                userphone =raw_input('请输入联系人电话：')
                addressBook[name] = userphone
                print(addressBook)
                continue
            else:
                continue
        else:
            userphone =raw_input('请输入联系人电话：')
            addressBook[name]=userphone
            print('联系人添加成功！')
            print(addressBook)
            continue
    if item == 3:    #删除联系人
        if name in addressBook:
            del addressBook[name]
            print('联系人删除成功！')
            print(addressBook)
            continue
        else:
            print('联系人不存在')
'''

'''
import os
folder = os.listdir('F:/APPIUMS_UI/jpg')#文件夹
print folder
if len(folder)>0:
    print '开始删除目录'
    for i in range(len(folder)):
        print i
        os.rmdir('F:/APPIUMS_UI/jpg/'+str(i))
    print '已删除目录'
else:
    print '不做删除动作'

'''

'''
import os
import shutil

def shutil_file(old_path=None,new_path_img0=None,new_path_img1=None):

    old_path='F:/APPIUMS_UI/jpg'
    picture = os.listdir(old_path)
    if len(picture) > 2:
        new_path_img0='F:/APPIUMS_UI/jpg/0'
        new_path_img1='F:/APPIUMS_UI/jpg/1'
        for i in picture:
            if i.split('-')[0] == '0Test':
                shutil.move(old_path+'/'+i,new_path_img0)
            elif i.split('-')[0] == '1Test':
                shutil.move(old_path+'/'+i,new_path_img1)
            else:
                print u'数据已移除完毕'
    elif len(picture) == 2:
        print u'数据已移除完毕'

    else:
        print u'数据错误'
'''

'''
import os 
a = os.listdir('F:/APPIUMS_UI/jpg')
if len(a) == 2:
    print 'ok'
else:
    print 'fail'
'''






