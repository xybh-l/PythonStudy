import requests
from bs4 import BeautifulSoup

url = 'http://www.xinhuanet.com/politics/2019-04/19/c_1124386249.htm'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
connect = requests.get(url,headers=headers)
connect.encoding = 'utf-8'
soup = BeautifulSoup(connect.content,'html.parser')
artical = []
artical = soup.select('.main-aticle')[0].text
print(artical)
# print(soup)