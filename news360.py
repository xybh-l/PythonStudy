import requests
from bs4 import BeautifulSoup
import json
import re

url = 'http://third.api.btime.com/News/shNews?callback=jQuery18302823528552239605_1556275623084&from=so&cid=1&os=win&timestamp=12232323&c=domestic&pos=1511174924289&c_pos=23226090&option=history&_=1556275716402'
res = requests.get(url)
# print(res.text)
reg = r'.+?\(\['
p1=re.compile(r'.+?\(\[')
p2=re.compile(r'\]\)')
m1=re.findall(p1,res.text)
m2=re.findall(p2,res.text)
# print(m1)
# print(m2)
text1 = re.sub(p1,"",res.text)
text2 = re.sub(p2,"",text1)
# file = open('E:\\VScode\\Python\\爬虫\\1.json',encoding='utf-8')
# text = file.read()
file = open('E:\\VScode\\Python\\爬虫\\1.json',encoding='utf-8')
for line in file.readlines():
    print(line)
    dic = json.loads(line)
# js =json.loads(text)
print(dic)
# print(js['u'])

