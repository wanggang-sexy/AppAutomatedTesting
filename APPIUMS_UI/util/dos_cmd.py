#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('F:/APPIUMS_UI')
import os
class DosCmd:
    def excute_cmd_result(self,command):
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def excute_cmd(self,command):
        return os.system(command)

    

if __name__ == '__main__':
    dos = DosCmd()
    print dos.excute_cmd_result('adb devices')
    #print dos.excute_cmd("adb devices")
    #print dos.excute_cmd('adb -s shell am start -W -n com.heshidai.app/.activity.finance.WelcomeActivity')#启动APP

    #print dos.excute_cmd('adb shell am force-stop com.heshidai.app')#杀掉APP进程
    dos.del_is_jpg('F:/APPIUMS_UI/jpg/0')



    



