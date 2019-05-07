from bs4 import BeautifulSoup
import requests

url = "http://news.sina.com.cn/china/"
res = requests.get(url)
print(res.status_code)
res.encoding = "utf-8";

print(type(res))
# print(str(res.text))
# print(res.headers)