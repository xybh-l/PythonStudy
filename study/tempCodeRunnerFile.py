import requests
from bs4 import BeautifulSoup
from lxml import etree


link = 'https://movie.douban.com/top250?start=50&filter='
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
def movietitle(link,i):
    f = open('E:\\VScode\\Python\\爬虫\\study\\movies\\movie{}.txt'.format(i),'w',encoding='utf-8')
    res = requests.get(link,headers=header).text
    soup = BeautifulSoup(res,'lxml')
    x = 1
    html = etree.HTML(res)
    titleol = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for title in titleol:
        titles1 = html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1]' .format(x))[0].text
        titles2 = html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[2]' .format(x))[0].text.strip()
        if len(html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span' .format(x))) == 3 :
            others = html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[3]' .format(x))
        else:
            titles2 = ''
            others = html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[2]' .format(x))
        # print(others[0].text.strip())
        f.write(titles1)
        f.write(titles2)
        f.write(others[0].text)
        f.write('\n')
        x=x+1
    print('抓取成功')
    f.close()

for i in range(0,10):
    link = 'https://movie.douban.com/top250?start={}&filter=' .format(i*25)
    movietitle(link,i+1)