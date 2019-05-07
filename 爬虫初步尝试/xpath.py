import requests
from lxml import etree


htmldata = requests.get('https://tieba.baidu.com/p/6115922278')

html = etree.HTML(htmldata.text)
words = html.xpath('//*[@id="post_content_125358073697"]/img/@src')
# //*[@id="post_content_125358073697"]/img[1]
# //*[@id="post_content_125358073697"]/img[2]
for w in words:
    print(w)