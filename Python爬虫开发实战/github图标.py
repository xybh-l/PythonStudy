import requests

headers = {
	'User-Agent':
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
r = requests.get("http://github.com/favicon.ico",headers=headers)
with open('favicon.ico', 'wb') as f:
	f.write(r.content)
