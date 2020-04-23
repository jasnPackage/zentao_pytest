#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Base():
    '''基于原生的selenium做第二次封装'''

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5


    def findElement(self,locator):
        '''定位到元素，返回元素对象，没定位到，Timeout异常'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id","value1")')
        else:
            print("正在定位元素信息：定位方式->%s，value值->%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
            return ele


    def findElements(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id","value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s，value值->%s" % (locator[0], locator[1]))
                eles = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
                return eles
            except:
                return []


    def sendKeys(self,locator,text=''):
        ele = self.findElement(locator)
        ele.send_keys(text)


    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()


    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()



    def isSelected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r


    def isElementExist(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False



    def is_title(self,_title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False



    def is_title_contains(self,_title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False



    def is_text_in_element(self,locator,_text=''):
        '''返回bool值'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id","value1")')
        else:
            try:
                result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
                return result
            except:
                return False



    def is_value_in_element(self,locator,_value=''):
        '''返回bool值，value为空字符串，返回False'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id","value1")')
        else:
            try:
                result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
                return result
            except:
                return False