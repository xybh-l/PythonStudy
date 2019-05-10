import requests
from lxml import etree

def gethtml(url):
    x = 1
    getimage(url,x)
    html = requests.get(url)
    html = etree.HTML(html.text)
    x = 2
    # alinks = html.xpath('//a[contains(string(), "下一页")]/@href')
    # while alinks:
    alinks = html.xpath('//a[contains(string(), "下一页")]/@href')
    link = 'http://tieba.baidu.com'+alinks[0]
    getimage(link,x)

def getimage(url,x):
    html = requests.get(url)
    html = etree.HTML(html.text)
    result = html.xpath('//img[@class="BDE_Image"]/@src')
    i = 0
    for image in result:
        with open('pic'+str(x)+str(i)+'.jpg','wb') as f:
            imageurl = requests.get(image)
            f.write(imageurl.content)
            print("抓取成功!")
        i = i+1

if __name__ == "__main__":
    gethtml('http://tieba.baidu.com/p/5962131817?pn=1')
