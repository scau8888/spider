# -*- coding: utf-8 -*-
from selenium import  webdriver
import time

driver_path=r"D:\chromedriver\chromedriver.exe"# 浏览器路径
driver=webdriver.Chrome(driver_path)#实例化
driver.get("https://www.baidu.com/")#打开网页
driver.execute_script("window.open('新URL')")#打开一个新网页
driver.switch_to_window(driver.window_handles[1])#切换到一个新的页面
#for driver in driver.get_cookies()#获取所有cookies的值
#value=driver.get_cookie(key)#获取某一个值的cookies
#driver.close()#关闭当前页面
#driver.quit()#退出浏览器
#by_id=driver.find_element_by_id("kw")#find_element_by_id通过id定位元素
#by_id=driver.find_element_by_class_name("s_ipt")#find_element_by_class_name通过类名定位元素
#html=driver.page_source#page_source获取页面html

by_id=driver.find_element_by_xpath("//input[@name='wd']")#find_element_by_xpath通过xpath定位元素

by_id.send_keys("python")#send_keys元素标签中填入python
time.sleep(3)
by_id=driver.find_element_by_id("su")

by_id.click()#点击标签

#by_id.clear()# clear清除标签里面的内容。

"""点击checkbox
操作checkbox（一个正方形小框，勾选要不要）,先选中chechbox标签，然后执行click事件。
by_id=driver.find_element_by_name("xxx")
by_id.click
"""
"""点击select标签
操作select标签，select元素不能直接点，需用类selenium.webdriver.support.ui.select,然后再选中哪一个
from selenium.webdriver.support.ui impot select
by_id=seclet(driver.find_element_by_name("xxx"))#创建选择对象
by_id.seclet_by_index(1) #通过标签选哪一个
"""


"""from selenium import  webdriver 行为链操作流程
from selenium.webdriver.common.action_chains import ActionChains

driver_path=r"D:\chromedriver\chromedriver.exe"# 浏览器路径
driver=webdriver.Chrome(driver_path)#实例化
driver.get("https://www.baidu.com/")#打开网页
inputTag=driver.find_element_by_id("kw")#定位输入框位置
submitbtn=driver.find_element_by_id("su")#定位输入数据后点击位置
action=ActionChains(driver)#调用行为函数实例化
action.move_to_element(inputTag)#移动到inputTag标签
action.send_keys_to_element(inputTag,"python")#标签中输入数据
action.move_to_element(submitbtn)#移动到点击按钮
action.click()#点击
action.perform()#启用链条
"""

""" 增加代理
from selenium import  webdriver

options=webdriver.ChromeOptions()#实例化opthons
options.add_argument("--proxy-server=http://代理ip：端口")#添加代理

driver_path=r"D:\chromedriver\chromedriver.exe"# 浏览器路径
driver=webdriver.Chrome(driver_path,chrome_options=options)#实例化时加入代理

driver.get("https://www.baidu.com/")#打开网页
"""