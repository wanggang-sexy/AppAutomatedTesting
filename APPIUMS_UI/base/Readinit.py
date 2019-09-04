#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import os
import sys
import string

class ReadIni(object):

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.file = 'F:APPIUMS_UI/config/LocalElement.ini'

    def read_ini(self):#读取文件
        self.config.read(self.file)

        '''
        section_list = self.config.sections()#获取主要列表
        print(section_list)

        option_list = self.config.options('baseconf')#获取单个信息下的所有列表
        print(option_list)

        item_list = self.config.items('baseconf')##获取某个列表信息
        print(item_list)
        '''
    def platformname(self):
        self.read_ini()
        platformname = self.config.get('login_element','mobile_login')
        return str(platformname)

    def apppackage(self):
        self.read_ini()
        apppackage = self.config.get('baseconf', 'apppackage')
        return apppackage

    def appactivity(self):
        self.read_ini()
        appactivity = self.config.get('baseconf', 'appactivity')
        return appactivity

    def deviceName(self):
        self.read_ini()
        deviceName = self.config.get('concurrent', 'deviceName')
        return deviceName

    def platformVersion(self):
        self.read_ini()
        platformVersion = self.config.get('concurrent', 'platformVersion')
        return platformVersion

if __name__ == "__main__":
    read = ReadIni()
    print read.platformname()



