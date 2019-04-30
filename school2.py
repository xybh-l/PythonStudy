import requests
from bs4 import BeautifulSoup
import urllib3
from lxml import etree
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def run(username,password):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'} #伪装浏览器
    url1 = 'https://webvpn1.ecit.cn/users/sign_in'
    s = requests.Session()
    res =  s.get(url1,verify=False,headers=header).text
    soup = BeautifulSoup(res,'html.parser')
    authenticity_token = soup.select("[name=authenticity_token]")[0].attrs['value']
    # print(authenticity_token)
    html = etree.HTML(res)
    # print(html)
    value = html.xpath('//*[@id="login-form"]/input[2]/@value')
    # print(value[0])
    # print(res)
    data = {
        'utf8':  '&#x2713;',
    'authenticity_token': value,
        'user[login]': username,
        'user[password]':password,
        'commit':'登录 Login'
    }
    res = s.post(url1,data=data,headers=header).text
    if '用户名或密码错误' in res:
        return 0
    if '此IP登录尝试次数过多' in res:
        return -1
    # print(res)
    url2 = 'https://cas-443.webvpn1.ecit.cn/login?service=https%3A%2F%2Fjw.webvpn1.ecit.cn%2Flogin.jsp'
    res = s.get(url2,verify=False,headers=header).text
    html = etree.HTML(res)
    Lt = html.xpath('//*[@id="login"]/form/ul/div/input/@value')
    # print(Lt[0])
    data = {
        'username': '201820180113',
        'password': '888999',
        'lt': Lt[0],
        'Submit':'' 
    }
    print('爬取中...')
    res = s.post(url2,data=data,verify=False,headers=header).text
    ticket = re.search("ticket=(.*)\"><img", res).group(1)
    url = 'https://jw.webvpn1.ecit.cn/login.jsp?ticket=' + ticket
    res = s.get(url,verify=False,headers=header).text
    url = 'https://jw.webvpn1.ecit.cn/reportFiles/student/cj_zwcjd_all.jsp?ticket=' + ticket
    res = s.get(url,verify=False,headers=header).text
    # print(url)
    url = 'https://jw.webvpn1.ecit.cn/syglSyxkAction.do?&oper=xsxkKcbAll'
    res = s.get(url,verify=False,headers=header).text
    f=open('timetable.html',mode='w',encoding='utf-8')
    f.write(res)
    print('爬取完成')
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
        print('登录成功！你的课表已保存在当前目录的timetable.hmtl文件，请用浏览器打开。')
    