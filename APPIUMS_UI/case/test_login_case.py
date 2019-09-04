# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
import unittest
import HTMLTestRunnerCN
import multiprocessing
import time
from main.action_method import ActionMethod
from util.server import Server
from util.write_user_command import WriteUserCommand
from util.dos_cmd import DosCmd
from util.del_folder import DelFolder


class ParameTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(ParameTestCase,self).__init__(methodName)
        self.parame = parame
        global parames
        parames = parame
class CaseTest(ParameTestCase):
    global parames
    @classmethod
    def setUpClass(cls):
        print u"= = = = = Start APP = = = = ="
        cls.action_method = ActionMethod(parames)
    def setUp(self):
        
        print u"= = = = = 开始执行用例 = = = = ="  
        
    def test_login_01(self):
        '''判断启动页面的轮播元素是都存在'''
        self.action_method.action_login_001(parames)

    def test_login_02(self):
        ''' 判断账户元素是否存在'''
        self.action_method.action_login_002(parames)

    def test_login_03(self):
        '''进入登录页面判断元素是否存在'''
        self.action_method.action_login_003(parames)

    def test_login_04(self):
        '''未输入内容，点击登录按钮'''
        self.action_method.action_login_004(parames)

    def test_login_05(self):
        '''输入账号，点击登录按钮'''
        self.action_method.action_login_005(parames)

    def test_login_06(self):
        '''输入密码点击登录按钮'''

        self.action_method.action_login_006(parames)

    def test_login_07(self):
        '''密码错误,点击登录'''

        self.action_method.action_login_007(parames)

    def test_login_08(self):
        '''账号错误'''

        self.action_method.action_login_008(parames)

    def test_login_09(self):
        '''账户或密码错误5次，锁定账户'''

        self.action_method.action_login_009(parames)

    def test_login_10(self):
        '''输入无效账号密码登录'''

        self.action_method.action_login_010(parames)

    def test_login_11(self):
        '''登录成功,设置手势密码'''

        self.action_method.action_login_011(parames)

    def test_login_12(self):
        '''判断弹窗，是否存在'''

        self.action_method.action_login_012(parames)

    def test_login_13(self):
        '''我的账户元素是否存在'''

        self.action_method.action_login_013(parames)

    def test_login_14(self):
        '''杀掉APP进程，再次启动APP'''

        self.action_method.action_login_014(parames)

    def test_login_15(self):
        '''手势密码解锁'''

        self.action_method.action_login_015()

    def test_login_16(self):
        '''判断弹窗，是否存在'''

        self.action_method.action_login_016(parames)

    def test_login_17(self):
        '''点击账户'''

        self.action_method.action_login_017()

    def test_login_18(self):
        '''退出APP登录'''

        self.action_method.action_login_018(parames)

    def test_login_19(self):
        '''切换普通登录'''

        self.action_method.action_login_019(parames)

    def test_login_20(self):
        '''未输入内容，进入普通用户登录'''

        self.action_method.action_login_020(parames)

    def test_login_21(self):
        '''输入账号，普通登录'''

        self.action_method.action_login_021(parames)

    def test_login_22(self):
        '''输入密码，普通登录'''

        self.action_method.action_login_022(parames)

    def test_login_23(self):
        '''密码错误，普通登录'''

        self.action_method.action_login_023(parames)

    def test_login_24(self):
        '''账号错误，普通登录'''

        self.action_method.action_login_024(parames)

    def test_login_25(self):
        '''账号或密码错误5次，账户锁定'''

        self.action_method.action_login_025(parames)

    def test_login_26(self):
        '''无效账户，普通登录'''

        self.action_method.action_login_026(parames)

    def test_login_27(self):
        '''普通登录成功，设置手势密码'''

        self.action_method.action_login_027(parames)

    def test_login_28(self):
        '''判断弹窗，是否存在'''

        self.action_method.action_login_028(parames)

    def test_login_29(self):
        '''我的账户元素是否存在'''

        self.action_method.action_login_029(parames)

    def test_login_30(self):
        '''杀掉APP进程，再次启动APP'''

        self.action_method.action_login_030(parames)

    def test_login_31(self):
        '''手势密码解锁'''
        self.action_method.action_login_031()


    def test_login_32(self):
        '''判断弹窗，是否存在'''
        self.action_method.action_login_032(parames)


    def test_login_33(self):
        '''点击账户'''
        self.action_method.action_login_033()


    def test_login_34(self):
        '''退出APP登录'''
        self.action_method.action_login_034(parames)

    def test_login_35(self):
        '''从登录页面返回首页'''
        self.action_method.action_login_035(parames)

    def test_login_36(self):
        '''输入手机号码，点击取消返回首页'''
        self.action_method.action_login_036(parames)


    def test_login_37(self):
        '''输入密码，点击取消返回首页'''
        self.action_method.action_login_037(parames)


    def test_login_38(self):
        '''输入手机号码和密码，点击取消返回首页'''
        self.action_method.action_login_038(parames)


    def test_login_39(self):
        '''输入手机和密码，切后台，5s，启动APP，数据存在'''
        self.action_method.action_login_039(parames)


    def test_login_40(self):
        '''输入手机和密码，杀掉进程，启动，数据不存在'''
        self.action_method.action_login_040(parames)


    def test_login_41(self):
        '''普通登录返回首页'''
        self.action_method.action_login_041(parames)


    def test_login_42(self):
        '''输入用户名，返回首页'''
        self.action_method.action_login_042(parames)


    def test_login_43(self):
        '''输入密码，返回首页'''
        self.action_method.action_login_043(parames)


    def test_login_44(self):
        '''输入用户名和密码，返回首页'''
        self.action_method.action_login_044(parames)


    def test_login_45(self):
        '''输入用户名和密码,切后台，等待5s，在启动，数据存在'''
        self.action_method.action_login_045(parames)


    def test_login_46(self):
        '''输入用户名和密码，杀掉进程，在启动，数据不存在，默认显示登录页面'''
        self.action_method.action_login_046(parames)

    def test_login_47(self):
        '''进入注册页面，元素存在'''
        self.action_method.registration_case_001(parames)

    def test_login_48(self):
        '''点击取消按钮，返回首页'''
        self.action_method.registration_case_002(parames)

    def test_login_49(self):
        '''输入小于11位手机号码'''
        self.action_method.registration_case_003(parames)

    def test_login_50(self):
        '''输入小于11位手机号码'''
        self.action_method.registration_case_003(parames)

    def test_login_51(self):
        '''输入大于11位手机号码'''
        self.action_method.registration_case_004(parames)

    def test_login_52(self):
        '''手机号码输入特殊字符'''
        self.action_method.registration_case_005(parames)

    def test_login_53(self):
        '''输入11位手机号码，获取验证码成功'''
        self.action_method.registration_case_006(parames)

    def test_login_54(self):
        '''同一账号，连续获取短信验证'''
        self.action_method.registration_case_007(parames)

    def test_login_55(self):
        '''重新获取短信验证码'''
        self.action_method.registration_case_008(parames)

    def test_login_56(self):
        '''未获取短信验证码，输入内容，提交验证'''
        self.action_method.registration_case_009(parames)

    def test_login_57(self):
        '''输入电话号码，点击提交验证'''
        self.action_method.registration_case_010(parames)

    def test_login_58(self):
        '''输入电话号码，输入错误的验证码，勾选协议，提交验证'''
        self.action_method.registration_case_011(parames)

    def test_login_59(self):
        '''输入手机号码和验证码，不勾选协议，提交验证'''
        self.action_method.registration_case_012(parames)

    def test_login_60(self):
        '''输入短信验证码小于6位数'''
        self.action_method.registration_case_013(parames)

    def test_login_61(self):
        '''输入短信验证码大于6位'''
        self.action_method.registration_case_014(parames)

    def test_login_62(self):
        '''输入已注册的账号'''
        self.action_method.registration_case_015(parames)

    def test_login_63(self):
        '''查看网站服务协议页面'''
        self.action_method.registration_case_016(parames)

    def test_login_64(self):
        '''查看风险提示书'''
        self.action_method.registration_case_017(parames)

    def test_login_65(self):
        '''进入设置密码页面'''
        self.action_method.registration_case_018(parames)

    def test_login_66(self):
        '''进入设置页面，不输入任何内容，点击完成完成设置'''
        self.action_method.registration_case_019(parames)

    def test_login_67(self):
        '''设置小于5位数登录密码'''
        self.action_method.registration_case_020(parames)

    def test_login_68(self):
        '''设置登录密码是6位纯数字'''
        self.action_method.registration_case_021(parames)

    def test_login_69(self):
        '''设置登录密码是特殊字符'''
        self.action_method.registration_case_022(parames)
    
    #def test_login_70(self):
        '''无效用例'''
    #   self.action_method.registration_case_023()


    def test_login_71(self):
        '''登录密码设置超过20个字符'''
        self.action_method.registration_case_024(parames)

    def test_login_72(self):
        '''设置登录密码成功，跳入设置手势密码页面,设置手势密码'''
        self.action_method.registration_case_025(parames)

    def test_login_73(self):
        '''注册成功'''
        self.action_method.registration_case_026(parames)

    def test_login_74(self):
        '''点击逛一逛按钮进入首页'''
        self.action_method.registration_case_027(parames)

    def test_login_75(self):
        '''退出APP'''
        self.action_method.registration_case_028(parames)






        
    def tearDown(self):
        
        print u"= = = = = 用例执行结束 = = = = ="
        
    @classmethod
    def tearDownClass(cls):
        print u"= = = = = Close APP = = = = ="
        cls.action_method.kill_App()#退出APP
        time.sleep(20)
        server = Server()
        server.kill_server()#杀掉appium服务进程
        
             

def appium_init():
    """
    启动appium服务
    """
    server = Server()
    server.main()#启动appium服务
   

def get_suit(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_login_01",parame=i))
    suite.addTest(CaseTest("test_login_02",parame=i))
    suite.addTest(CaseTest("test_login_03",parame=i))
    suite.addTest(CaseTest("test_login_04",parame=i))
    suite.addTest(CaseTest("test_login_05",parame=i))
    suite.addTest(CaseTest("test_login_06",parame=i))
    suite.addTest(CaseTest("test_login_07",parame=i))
    suite.addTest(CaseTest("test_login_08",parame=i))
    suite.addTest(CaseTest("test_login_09",parame=i))
    suite.addTest(CaseTest("test_login_10",parame=i))
    suite.addTest(CaseTest("test_login_11",parame=i))
    suite.addTest(CaseTest("test_login_12",parame=i))
    suite.addTest(CaseTest("test_login_13",parame=i))
    suite.addTest(CaseTest("test_login_14",parame=i))
    suite.addTest(CaseTest("test_login_15",parame=i))
    suite.addTest(CaseTest("test_login_16",parame=i))
    suite.addTest(CaseTest("test_login_17",parame=i))
    suite.addTest(CaseTest("test_login_18",parame=i))
    suite.addTest(CaseTest("test_login_19",parame=i))
    suite.addTest(CaseTest("test_login_20",parame=i))
    suite.addTest(CaseTest("test_login_21",parame=i))
    suite.addTest(CaseTest("test_login_22",parame=i))
    suite.addTest(CaseTest("test_login_23",parame=i))
    suite.addTest(CaseTest("test_login_24",parame=i))
    suite.addTest(CaseTest("test_login_25",parame=i))
    suite.addTest(CaseTest("test_login_26",parame=i))
    suite.addTest(CaseTest("test_login_27",parame=i))
    suite.addTest(CaseTest("test_login_28",parame=i))
    suite.addTest(CaseTest("test_login_29",parame=i))
    suite.addTest(CaseTest("test_login_30",parame=i))
    suite.addTest(CaseTest("test_login_31",parame=i))
    suite.addTest(CaseTest("test_login_32",parame=i))
    suite.addTest(CaseTest("test_login_33",parame=i))
    suite.addTest(CaseTest("test_login_34",parame=i))
    suite.addTest(CaseTest("test_login_35",parame=i))
    suite.addTest(CaseTest("test_login_36",parame=i))
    suite.addTest(CaseTest("test_login_37",parame=i))
    suite.addTest(CaseTest("test_login_38",parame=i))
    suite.addTest(CaseTest("test_login_39",parame=i))
    suite.addTest(CaseTest("test_login_40",parame=i))
    suite.addTest(CaseTest("test_login_41",parame=i))
    suite.addTest(CaseTest("test_login_42",parame=i))
    suite.addTest(CaseTest("test_login_43",parame=i))
    suite.addTest(CaseTest("test_login_44",parame=i))
    suite.addTest(CaseTest("test_login_45",parame=i))
    suite.addTest(CaseTest("test_login_46",parame=i))
    suite.addTest(CaseTest("test_login_47",parame=i))
    suite.addTest(CaseTest("test_login_48",parame=i))
    suite.addTest(CaseTest("test_login_49",parame=i))
    suite.addTest(CaseTest("test_login_50",parame=i))
    suite.addTest(CaseTest("test_login_51",parame=i))
    suite.addTest(CaseTest("test_login_52",parame=i))
    suite.addTest(CaseTest("test_login_53",parame=i))
    suite.addTest(CaseTest("test_login_54",parame=i))
    suite.addTest(CaseTest("test_login_55",parame=i))
    suite.addTest(CaseTest("test_login_56",parame=i))
    suite.addTest(CaseTest("test_login_57",parame=i))
    suite.addTest(CaseTest("test_login_58",parame=i))
    suite.addTest(CaseTest("test_login_59",parame=i))
    suite.addTest(CaseTest("test_login_60",parame=i))
    suite.addTest(CaseTest("test_login_61",parame=i))
    suite.addTest(CaseTest("test_login_62",parame=i))
    suite.addTest(CaseTest("test_login_63",parame=i))
    suite.addTest(CaseTest("test_login_64",parame=i))
    suite.addTest(CaseTest("test_login_65",parame=i))
    suite.addTest(CaseTest("test_login_66",parame=i))
    suite.addTest(CaseTest("test_login_67",parame=i))
    suite.addTest(CaseTest("test_login_68",parame=i))
    suite.addTest(CaseTest("test_login_69",parame=i))
    #suite.addTest(CaseTest("test_login_70",parame=i))
    suite.addTest(CaseTest("test_login_71",parame=i))
    suite.addTest(CaseTest("test_login_72",parame=i))
    suite.addTest(CaseTest("test_login_73",parame=i))
    suite.addTest(CaseTest("test_login_74",parame=i))
    suite.addTest(CaseTest("test_login_75", parame=i))
    
    


    #unittest.TextTestRunner().run(suite)
    
    #按照一定格式获取当前时间
    Now = time.strftime("%Y%m%d_%H%M%S")
    html_file = "F:/APPIUMS_UI/report/report"+Now+".html"
    fp = file(html_file,"wb")
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告', 
        #description='详细测试用例结果',    #不传默认为空
        tester=u"Wanggang"     #测试人员名字，不传默认为QA
        )
    runner.run(suite)
    
    


def get_count():
    """
    获取设备数量
    """
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


def del_picture():
    """
    删除原来的图片
    """
    dels = DelFolder()
    dels.del_is_jpg()

if __name__ == "__main__":
    
    appium_init()#启动服务
    time.sleep(15)
    
    del_picture()#清除本地已有的截图
    
    time.sleep(5)
    threds = []
    for i in range(get_count()):
        t = multiprocessing.Process(target=get_suit,args=(i,))
        threds.append(t)
    for j in threds:
        j.start()
        time.sleep(5)
    
    
    