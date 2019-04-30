import requests
from bs4 import BeautifulSoup

link = 'http://www.santostang.com/'
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
r = requests.get(link,headers = header)
soup = BeautifulSoup(r.text,'lxml')
title = soup.find('h1', class_="post-title").a.text.strip()
print(title)
