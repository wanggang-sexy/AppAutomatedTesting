#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from dos_cmd import DosCmd
class Port(object):
    def port_is_used(self,port_num):
        """
        判断端口是否被占用
        """
        flag = None
        self.dos = DosCmd()
        command = "netstat -ano | findstr "+str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def creat_port_list(self,start_port,device_list):
        """
        生成可用端口
        :param start_port:
        :param device_list:
        """
        port_list = []
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) != True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print "生成可用端口失败"
            return None


if __name__ == "__main__":
    port = Port()
    device_list = [1,2,3,4]
    print port.creat_port_list(4720,device_list)
