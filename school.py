def run(username,password):
    import requests
    import re
    from bs4 import BeautifulSoup
    import urllib3
    import random
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'} #伪装浏览器
    s = requests.Session()                          #创建session对象
    url = 'https://webvpn1.ecit.cn/users/sign_in'   
    res = s.get(url,verify=False,headers=header).text
    soup = BeautifulSoup(res,'html.parser')
    authenticity_token = soup.select("[name=authenticity_token]")[0].attrs['value']
    print(type(authenticity_token))
    data = {
        'utf8' : '&#x2713;',
        'authenticity_token' : authenticity_token,
        'user[login]' : username,
        'user[password]' : password,
        'commit' : '登录 Login'
    }
    res = s.post(url,data=data,verify=False,headers=header).text
    if '用户名或密码错误' in res:
        return 0
    if '此IP登录尝试次数过多' in res:
        return -1
    url = 'https://cas-443.webvpn1.ecit.cn/login?service=https%3A%2F%2Fjw.webvpn1.ecit.cn%2Flogin.jsp'
    res = s.get(url,verify=False,headers=header).text
    soup = BeautifulSoup(res,'html.parser')
    lt = soup.select("[name=lt]")[0].attrs['value']
    data = {
        'username' : username,
        'password' : password,
        'lt' : lt,
        'Submit' : ''
    }
    res = s.post(url,data=data,verify=False,headers=header).text
    # print(res)
    ticket = re.search("ticket=(.*)\"><img", res).group(1)
    url = 'https://jw.webvpn1.ecit.cn/login.jsp?ticket=' + ticket
    res = s.get(url,verify=False,headers=header).text
    url = 'https://jw.webvpn1.ecit.cn/reportFiles/student/cj_zwcjd_all.jsp?ticket=' + ticket
    res = s.get(url,verify=False,headers=header).text
    # print(res)
    f=open('score.html',mode='w',encoding='utf-8')
    f.write(res)
    return 1

if __name__ == "__main__":
    username = input('请输入你的学号：')
    password = input('请输入你的密码：')
    status = run(username,password)
    print(status)
    if status == -1:
        print('此IP登录尝试次数过多')
    elif status == 0:
        print('账号或密码错误')
    elif status == 1:
        print('登录成功！你的成绩信息已保存在当前目录的score.hmtl文件，请用浏览器打开。')

run(username,password)