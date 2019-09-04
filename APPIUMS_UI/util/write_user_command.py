#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import os

class WriteUserCommand(object):
    def read_data(self):
        """
        加载yaml数据
        """
        with open("F:/APPIUMS_UI/config/userconfig.yaml") as fr:
            data = yaml.load(fr)
        return data


    def get_value(self,key,port):
        """
        获取数据
        """
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self,i,device,bp,port,platformVersion):
        """
        写入数据
        """
        data = self.join_data(i,device,bp,port,platformVersion)
        with open("F:/APPIUMS_UI/config/userconfig.yaml","a") as fr:
            yaml.dump(data,fr)

    def join_data(self,i,device,bp,port,platformVersion):
        """
        数据拼接
        """
        data = {
        "user_info_"+str(i):{
        "deviceName":device,
        "bp":bp,
        "port":port,
        "platformVersion":platformVersion
        }
        }
        return data

    def clear_data(self):
        """
        清除原有的旧数据
        """
        with open("F:/APPIUMS_UI/config/userconfig.yaml","w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        """
        统计数据有多行
        """
        data = self.read_data()
        return len(data)


if __name__ == "__main__":
    write = WriteUserCommand()
    print write.read_data()
    print type(write.read_data())
    print write.get_value('user_info_0','bp')
    
    
    


    


    
    
 
