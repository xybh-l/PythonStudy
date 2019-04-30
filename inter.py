import requests

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res = requests.get('http://172.21.255.105/a79.htm?userip=172.22.6.255&wlanacname=&wlanacip=172.21.255.106&usermac=08d79552a7d61237308ab28bca5bbc15d72025294c800570',headers= header)

print(res.status_code)
print(res.text)