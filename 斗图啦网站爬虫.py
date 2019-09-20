# -*- coding: utf-8 -*-

import requests
from lxml import etree
from urllib import request
#import os
import re

def parse(url):
     headers={
         'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
     }
     reponse=requests.get(url,headers=headers)
     text=reponse.content.decode()
     html=etree.HTML(text)

     imgs=html.xpath("//div[@class='col-sm-9 center-wrap']//img[@class!='gif']")#分组

     for img in imgs:
         #img_url=img.get("data-original")# get 直接取到url
         img_url=img.xpath("./@data-original")[0] #xpath先得到列表，在取值
         alt=img.xpath("./@alt")[0]
         alt=re.sub(r'[\?\.!！，。？:]',"",alt)#windows很多特殊符号不能作为文件名，需用sub函数替换掉。可用[]括起来。
         #suffix=os.path.splitext(img_url)[1]#利用OS模块的splitext函数讲URL分割成www.xxxx和.img。
         suffix=img_url[-4:]
         filename=alt+suffix
         request.urlretrieve(img_url,"img/"+filename)#img_url图片地址，"img/"文件夹，filename保存文件的名字。

def main():
    for x in range(1,5):
        url='http://www.doutula.com/article/list/?page=%d'%x
        parse(url)

if __name__ == '__main__':
   main()