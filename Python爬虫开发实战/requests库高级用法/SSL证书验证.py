import requests

response = requests.get('https://study.lanwang.online', verify=False)
print(response.status_code)