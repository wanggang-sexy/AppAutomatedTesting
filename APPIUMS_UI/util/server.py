# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from dos_cmd import DosCmd
from port import Port
import threading
import time
from write_user_command import WriteUserCommand
import os

class Server(object):
    def __init__(self):
        self.dos = DosCmd()
        self.port = Port()
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommand()


    def get_devices(self):
        '''
        获取设备信息
        '''
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:

            return None


    def get_platformVersion(self,i):
        """
        获取设备系统
        """
        platform_version_list = []
        device_list = self.device_list
        platform_version = self.dos.excute_cmd_result("adb -s "+device_list[i]+" shell getprop ro.build.version.release")
        if len(platform_version) > 0:
            for i in platform_version:
                platform_version_info = i.split('\r')
                platform_version_list.append(platform_version_info[0])
        return platform_version_list[0]

    def get_start_app(self,i):
        """
        启动APP
        """
        device_list = self.device_list
        self.dos.excute_cmd("adb -s "+device_list[i]+" shell am start -W -n com.heshidai.app/.activity.finance.WelcomeActivity")

    def kill_app(self,i):
        """
        杀掉APP进程
        """
        device_list = self.device_list
        self.dos.excute_cmd("adb -s "+device_list[i]+" shell am force-stop com.heshidai.app")

    def cut_background(self,i):
        """
        应用切后台
        """
        device_list = self.device_list
        self.dos.excute_cmd("adb -s "+device_list[i]+" shell input keyevent 3")


    def creat_port_list(self,start_port):
        """
        创建可用端口
        """
        port_list = []
        port_list = self.port.creat_port_list(start_port,self.device_list)
        return port_list

    def creat_command_list(self,i):
        """
        生成对应的appiu启动数据
        appium - p 4700 -bp 4900 -U （DEVICE）号
        """

        command_list = []
        appium_port_list = self.creat_port_list(4700)
        bootstrap_port_list = self.creat_port_list(4900)
        device_list = self.device_list
        command = "appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override --log F:/APPIUMS_UI/log/"+str(int(time.time()))+".log"
        #appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log E:/Teacher/Imooc/AppiumPython/log/test01.log
        command_list.append(command)
        self.write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]),str(self.get_platformVersion(i)))
        return command_list


    def start_server(self,i):
        """
        启动appium服务
        """
        start_list = self.creat_command_list(i)
        print start_list
        self.dos.excute_cmd(start_list[0])


    def kill_server(self):
        """
        启动服务之前，先杀掉原先已有的appium服务
        """
        server_list = self.dos.excute_cmd_result("tasklist | findstr node.exe")
        if len(server_list) > 0:
            self.dos.excute_cmd("taskkill -F -PID node.exe")

    def main(self):
        """
        多线程启动appium服务
        """
        #thread_list = []
        self.kill_server()
        time.sleep(5)
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server,args=(i,))
            appium_start.start()
        time.sleep(20)

        '''
        for j in thread_list:
            j.start()
            time.sleep(25)
        '''

if __name__ == "__main__":

    servers = Server()
    servers.kill_server()












