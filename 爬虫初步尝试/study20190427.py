import requests
import re
import os
import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import sys
import importlib
importlib.reload(sys) #解决'ascii' codec can't encode characters in position 83-87: ordinal not in range(128)问题

def gethtml(url):
    heads = {}
    heads['User-Agent'] = 'Mozilla/5.0 ' \
                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'
    html = requests.get(url,headers = heads)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.content,'html.parser')
    reg = r'href="(\/p\/.+?)" '
    rhtml = re.compile(reg)
    rehtml = re.findall(rhtml, html.text)
    l=1
    for r in rehtml[1:]:
        r = urllib.parse.quote(r)
        endhtml = 'https://tieba.baidu.com' + r 
        print(endhtml)
        getimage(endhtml,l)
        l += 1

def getimage(html,l):
    html1 = requests.get(html)
    html1.encoding = 'utf-8'
    path = "D:\\images\\women\\%s\\" %l
    reg1 = r'src="(.+?\.jpg)" size'
    reg2 = r'height=".+?" src="(.+?\.jpg)"'
    image1 = re.compile(reg1)
    image2 = re.compile(reg2)
    if not os.path.exists(path):  # 判断该文件夹是否存在，不存在则创建
        os.mkdir(path)
    x= 0
    imglist = re.findall(image1 or image2, html1.text)
    length = len(imglist)
    i = 1
    for img in imglist:
        try:
            # img = urllib.parse.quote(img[6:])
            # img = "https:" + img;
            urllib.request.urlretrieve(img, path+'%s.jpg' % x)
        except urllib.error.HTTPError as e:
            print("抓取失败! 已抓取[%s/%s]" %(i,length))
            continue
        else:
            print(path+'%s.jpg 已抓取[%s/%s]' %(x,i,length))
            x += 1
        i+=1
        
       

gethtml('https://tieba.baidu.com/f?kw=%C3%C0%C5%AE&fr=ala0&tpl=5')
# gethtml('https://tieba.baidu.com/f?kw=%CD%BC%C6%AC&fr=ala0&tpl=5')