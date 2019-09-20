# -*- coding: utf-8 -*-

import requests
from lxml import etree
from urllib import request
#import os
import re
from queue import Queue
import threading

class Procuder(threading.Thread):
    headers={
         'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
     }
    def __init__(self,page_queue,image_queue,*args,**kwargs):#构造函数，将page_queue,image_queue两参数传入
        super(Procuder,self).__init__(*args,**kwargs)#重写父类函数
        self.page_queue=page_queue#实例化类属性
        self.image_queue=image_queue

    def run(self):

        while True:# 循环请求。
            if self.page_queue.empty():#避免死循环，增加判断，当为空时，退出。
                break
            url=self.page_queue.get()#从队列中获取页面URL
            self.parse(url)
    def parse(self,url):
         reponse=requests.get(url,headers=self.headers)
         text=reponse.content.decode()
         html=etree.HTML(text)

         imgs=html.xpath("//div[@class='col-sm-9 center-wrap']//img[@class!='gif']")#分组

         for img in imgs:
            #img_url=img.get("data-original")# get方法可以 直接取到url
             img_url=img.xpath("./@data-original")[0] #xpath先得到列表，在取值
             alt=img.xpath("./@alt")[0]
             alt=re.sub(r'[\?\.!！，。？:]',"",alt)#windows很多特殊符号不能作为文件名，需用sub函数替换掉。可用[]括起来。
         #suffix=os.path.splitext(img_url)[1]#利用OS模块的splitext函数讲URL分割成www.xxxx和.img。
             suffix=img_url[-4:]#切片取后四位
             filename=alt+suffix
             self.image_queue.put((img_url,filename))
class Consumer(threading.Thread):
    def __init__(self,page_queue,image_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue=page_queue
        self.image_queue=image_queue
    def run(self):
        while True:
            if self.image_queue.empty() and self.page_queue.empty():
                break
            img_url,filename=self.image_queue.get()
            request.urlretrieve(img_url,"img/"+filename)#img_url图片地址，"img/"文件夹，filename保存文件的名字。
            print(filename)


def main():
    page_queue=Queue(100)
    image_queue=Queue(1000)# 队列数最大为1000
    for x in range(1,50):
        url='http://www.doutula.com/article/list/?page=%d'%x
        page_queue.put(url)
    for x in range(5):#创建5个生产者线程
        t=Procuder(page_queue,image_queue)
        t.start()

    for x in range(5):#创建5个消费者线程
        t=Consumer(page_queue,image_queue)
        t.start()

if __name__ == '__main__':
   main()

"""逻辑思路：
用消费生产者模型，生产者往队列中添加图片URL，消费者从队列中取url然后保存图片。
1、创建主函数main，创建页面队列（page_queue），图片队列（image_queue）。把页面URL添加到页面队列中。
2、创建生产者类，创建构造函数_init_》重写父类，实例化页面队列（page_queue），图片队列（image_queue）两个属性。
   ①、创建run函数从页面队列（page_queue）取出页面URL。
   ②、创建 parse函数，请求页面，解析页面，获得图片URL，添加到图片队列中。
   ③、run函数调用parse函数。

3、创建消费者类，创建构造函数_init_》重写父类，实例化页面队列（page_queue），图片队列（image_queue）两个属性。
   ①、创建run函数从图片队列（image_queue）取出页面URL。
   ②、保存图片。
"""