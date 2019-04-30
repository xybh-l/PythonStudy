import requests
import re
import os
import sys
from bs4 import BeautifulSoup

def gethtml(url):
    heads = {}
    heads['User-Agent'] = 'Mozilla/5.0 ' \
                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'
    html = requests.get(url,headers = heads)
    html.encoding = 'utf-8'
    # print(html.text)
    # soup = BeautifulSoup(html.content,'html.parser')
    reg = r"href='(.+?\/page\.htm)'"
    rhtml = re.compile(reg)
    rehtml = re.findall(rhtml, html.text)
    print(rehtml)
    l=1
    for r in rehtml:
        # r = urllib.parse.quote(r)
        endhtml = 'http://news.ecut.edu.cn' + r 
        print(endhtml)
        # getimage(endhtml,l)
        artical(endhtml)
        l += 1

def artical(html):
    html1 = requests.get(html)
    soup = BeautifulSoup(html1.content,'html.parser')
    title = soup.select('.arti_title')[0].text.strip()
    art = soup.select('.wp_articlecontent p')
    if not os.path.exists('\\WEB\\news\\'+title+'.txt'): 
        with open('\\WEB\\news\\'+title+'.txt','w',encoding='utf-8') as f:
            for a in art:
             f.write("{}".format(a.text))
    else:
        with open('\\WEB\\news\\'+title+'.txt','a',encoding='utf-8') as f:
            for a in art:
             f.write("{}".format(a.text))
             f.write('\n')
    
    

gethtml('http://news.ecut.edu.cn/120/list.htm')
# artical('http://news.ecut.edu.cn/03/8b/c120a66443/page.htm')