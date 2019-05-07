import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

res = requests.get('https://news.sina.com.cn/c/2019-04-23/doc-ihvhiewr7873518.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.content,'html.parser')
print(soup.select('.main-title')[0].text)
# print(soup.select('#reg_header .reg_h_center .reg_h_left h3')[0].text)
timesource = soup.select('.date-source')[0].contents[1].text.strip()
dt = datetime.strptime(timesource,'%Y年%m月%d日 %H:%M')
source = soup.select('.date-source a')[0].text
print(source)
print(dt)
article = []
[article.append(p.text.strip()) for p in soup.select('#article p')[:-1]]
print(' '.join(article))
print(soup.select('.show_author')[0].text)
comment = requests.get('https://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-hvhiewr7873518&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1&uid=unlogin_user')
jd = comment.json()
print(jd['result']['count']['total'])
# jd = json.loads(comment.text)
# print(jd)
# print(jd['result']['count']['total'])
# comment = soup.select('#top_bar .page-tools .tool-cmt  a .num')
# print(comment)