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

     imgs=html.xpath("//div[@class='col-sm-9 center-wrap']//img[@class!='gif']")


     for img in imgs:
         #print(etree.tostring(img))
         #img_url=img.get("data-original")
         img_url=img.xpath("./@data-original")[0]
         #print(img_url)
         #print(img_url)
         alt=img.xpath("./@alt")[0]
         alt=re.sub(r'[\?\.!！，。？:]',"",alt)
         #suffix=os.path.splitext(img_url)[1]
         suffix=img_url[-4:]
         filename=alt+suffix
         request.urlretrieve(img_url,"img/"+filename)


def main():
    for x in range(1,5):
        url='http://www.doutula.com/article/list/?page=%d'%x

        parse(url)

if __name__ == '__main__':
   main()