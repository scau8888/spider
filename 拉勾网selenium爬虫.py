from selenium import  webdriver
from  lxml import etree
import re
import time
class LaGouSpiDer:
     def __init__(self):
         self.driver_path=r"D:\chromedriver\chromedriver.exe"# 浏览器路径
         self.driver=webdriver.Chrome(self.driver_path)#实例化


     def run(self):#主函数
         self.driver.get("https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py")#请求首页
         while True:#循环请求
             source=self.driver.page_source#获取首页HTML
             link=self.parse_page_list(source)#调用函数，获取详情页URL
             next_page=self.driver.find_element_by_class_name("pager_next ")#定位下一页按钮，
             next_page.click()#点击下一页按钮
             time.sleep(3)


     def parse_page_list(self,source):#获取详情页URL
         html=etree.HTML(source)
         links=html.xpath("//li//a[@class='position_link']/@href")#分组
         for link in links:#遍历详情页URL
             self.request_detail_list(link)#调用函数，请求详情页

     def request_detail_list(self,link):#请求详情页
         self.driver.execute_script("window.open('%s')"%link)#打开新窗口，请求详情页
         self.driver.switch_to.window(self.driver.window_handles[1])#转到详情页
         #self.driver.get(link)
         detail_source = self.driver.page_source#获取详情页资源
         self.parse_detail_list(detail_source)#调用函数，解析详情页
         self.driver.close()#关闭新窗口
         self.driver.switch_to.window(self.driver.window_handles[0])#转到首页窗口


     def parse_detail_list(self,detail_source):#解析详情页，获取想要的信息
          html=etree.HTML(detail_source)
          postion=html.xpath("//div[@class='ceil-left']//span[@class='ceil-job']/text()")[0]
          postions=re.sub(r"[\s/]"," ",postion)
          salary=html.xpath("//div[@class='ceil-left']//span[@class='ceil-salary']/text()")[0]
          salarys=re.sub(r"[\s/]"," ",salary)
          detal=html.xpath("//dd[@class='job_request']//span/text()")[1]
          detals=re.sub(r"[\s/]"," ",detal)
          xiangxi=html.xpath("//div[@class='job-detail']//p/text()")
          item={}
          item["职位"]=postions
          item["工资"]=salarys
          item["详细"]=xiangxi
          item["地址"]=detals
          print(item)
         #html=etree.HTML(source)
if __name__ == '__main__':
    spider=LaGouSpiDer()
    spider.run()

"""用类方法实现selenium爬拉钩网。
导入selenium》定义一个类，webdriver.Chrome、driver_path作为类属性》加主程序、主函数run方法》run方法使用driver.get打开页面
获取html》定义一个函数解析html，获取详情页URL 》定义一个函数请求详情页（请求详情页需打开一个新窗口，转到新窗口，获取资源，关闭新窗口，循环请求）》
定义一个函数解析详情页内容，获取数据。——————》run方法请求首页循环，找到下一页按钮，点击下一页。
"""
