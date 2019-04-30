import requests
from bs4 import BeautifulSoup
from lxml import etree


link = 'https://movie.douban.com/top250?start=50&filter='
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
def movietitle(link,i):
    f = open('E:\\VScode\\Python\\爬虫\\study\\movie{}.txt'.format(i),'w',encoding='utf-8')
    res = requests.get(link,headers=header).text
    x = 1
    html = etree.HTML(res)
    titleol = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for title in titleol:
        titles1 = html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1]' .format(x))
        titles2 = html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[2]' .format(x))
        play = html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/span' .format(x)).text
        # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/span
        # //*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[1]/span
        print(play)
        if  play[0].text == '':
            playable = '可播放'
        # else:
        #     playable = '不可播放'
        # # others = html.xpath('//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[3]' .format(x))
        # # print(others[0].text.strip())
        # f.write(titles1[0].text)
        # f.write(titles2[0].text.strip())
        # f.write(playable)
        # # f.write(other[0].text)
        # f.write('\n')
        # x=x+1
    print('抓取成功')
    f.close()

for i in range(0,10):
    link = 'https://movie.douban.com/top250?start={}&filter=' .format(i*25)
    movietitle(link,i+1)