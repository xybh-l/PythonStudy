import requests
import os
import shutil
from lxml import etree

def mkdir(url):
    if url[:5] == 'https':
        url = url.lstrip("https://tieba.baidu.com/p/")
    else:
        url = url.lstrip("http://tieba.baidu.com/p/")
    dir = 'E:\VScode\Python\爬虫\PythonStudy\自我尝试\\' + url
    if os.path.exists("E:\VScode\Python\爬虫\PythonStudy\自我尝试\\{url}".format(url=url)):
        choice = input('该网站已抓取,是否更新(y/n):')
        if choice == 'n':
           return
        else:
          shutil.rmtree(dir)
    os.makedirs(dir)
    return dir

def gethtml(url):
    link = url
    x = 1
    begin = 0
    while 1:
        try:
            if begin == 0:
                dir = mkdir(url)
                begin = 1
            res = getimage(link,x,dir)
            if res == 0:
                return
            print("已抓取"+str(x)+"页")
            html = requests.get(link)
            html = etree.HTML(html.text)
            alinks = html.xpath('//a[contains(string(), "下一页")]/@href')
            link = 'http://tieba.baidu.com'+alinks[0]
            x = x + 1
        except Exception as e:
            print("已到最后一页!")
            break

def getimage(url,x,dir):
    html = requests.get(url)
    html = etree.HTML(html.text)
    n = 1
    result = html.xpath('//img[@class="BDE_Image"]/@src')
    if result == []:
        return 0
    i = 10
    for image in result:
        with open(dir+'\pic'+str(x)+str(i)+'.jpg','wb') as f:
            imageurl = requests.get(image)
            f.write(imageurl.content)
        i = i+1

if __name__ == "__main__":
    # gethtml('http://tieba.baidu.com/p/5962131817?pn=1')
    # gethtml('http://tieba.baidu.com/p/6127270045')
    # gethtml('http://tieba.baidu.com/p/6013941026')
    gethtml('http://tieba.baidu.com/p/6126335781')
    # gethtml('https://tieba.baidu.com/p/6126863907')
