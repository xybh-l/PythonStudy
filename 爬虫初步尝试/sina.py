import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup =  BeautifulSoup(res.text,"html.parser")

for news in soup.select('.feed-card-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        time = news.select('feed-card-time')[0].text
        a = news.select('a')[0]['href']
        print(a,time)