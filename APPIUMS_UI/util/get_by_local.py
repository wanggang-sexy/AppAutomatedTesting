#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('F:/APPIUMS_UI')
from util.read_init import ReadIni

class GetByLocal(object):

    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key,section=None):
        read_ini = ReadIni()
        local = read_ini.get_element_value(key,section)
        print local
        
        if local != None:
            by = local.split(">")[0]
            loacal_by = local.split(">")[1]
            loacal_bys = local.split(">")[2]    
            try:
                if by == "id":
                    return self.driver.find_element_by_id(loacal_by)
                elif by == "classname":
                    return self.driver.find_element_by_class_name(loacal_by)
                elif by == "text":
                    return self.driver.find_element_by_name(loacal_by)#find_element_by_android_uiautomator('new UiSelector().text(loacal_by)')
                elif by == "class":
                    element = self.driver.find_element_by_id(loacal_by)
                    return element.find_elements_by_class_name(loacal_bys)
                elif by == "link":
                    return self.driver.find_element_by_link_text(loacal_by)
                else:
                    return self.driver.find_element_by_xpath(loacal_by)
            except:
                return None
            
        else:
            return None

    