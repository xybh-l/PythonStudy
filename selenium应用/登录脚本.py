from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
import time
import re
import os
import win32com
import traceback

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://172.21.255.105/")
except:
        print ("traceback.format_exc():\n%s" % traceback.format_exc())

string1 = ''
TIME = 0.6


# 读取本地记录
def Read(i):
    global user, pwd, choice1
    if i == 1:
        if os.path.exists("D:\\schoolnetwork.data"):
            with open("D:\\schoolnetwork.data", "r") as f:
                user = str(f.readline()).strip()
                pwd = str(f.readline()).strip()
                choice1 = str(f.readline()).strip()
                f.close()
        else:
            data = input("数据不存在,是否保存数据(y/n):")
            if data == 'y':
                with open("D:\\schoolnetwork.data", "w") as f:
                    f.write(input("用户名:"))
                    f.write(input("密码:"))
                    f.write(input("请输入网络服务运行商(1.移动 2.电信 3.联通 4.校园网):"))
                    f.close()
    if i == 2:
        data = input("是否保存账号密码(y/n):")
        if data == 'y':
            with open("D:\\schoolnetwork.data", "w") as f:
                f.write(str(user))
                f.write('\n')
                f.write(str(pwd))
                f.write('\n')
                f.write(str(choice1))
                f.close()

# 检测是否已经登录
def Check():
    time.sleep(TIME)
    try:
        string1 = driver.find_element_by_xpath('//*[@id="edit_body"]/div[1]/div[1]/form/input').get_attribute("value")
    except Exception:
        UP()
    finally:
        if (string1 == '注  销'):
            rlogin = input('你已登录,是否要重新登录(y/n):')
            if rlogin == 'y':
                logout = driver.find_element_by_xpath('//*[@id="edit_body"]/div[1]/div[1]/form/input')
                print("注销中...")
                logout.click()
                affirm = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/input[1]')
                affirm.click()
                time.sleep(TIME)
                driver.refresh()
                time.sleep(TIME)
                UP()
            if rlogin == 'n':
                driver.close();


# 选择登录方式
def UP():
    global choice1, user, pwd
    choice = input('1.自动登录 2.手动登录:')
    x = 1
    while x == 1:
        if choice == '1':
            Read(1)
            x = 0
        elif choice == '2':
            choice1 = input('请输入网络服务运行商(1.移动 2.电信 3.联通 4.校园网):')
            choice1 = int(choice1) + 1
            user = input('请输入用户名:')
            pwd = input('请输入密码:')
            x = 0
            Read(2)
        else:
            choice = input('请重新输入:')
            x = 1
    Connect()


# 进行登录连接
def Connect():
    global choice1, pwd, user
    try:
        loginable = []
        loginable = driver.get('//*[@id="edit_body"]/div[1]/div[1]/form/input').text
        print(loginable)
    except Exception as i:
        pass

    try:
        message = driver.get('//*[@id="message"]').text
    except Exception as id:
        pass
    else:
        print("密码错误!")
    try:
        ispchoice = '//*[@id="edit_body"]/div[2]/div[2]/div/span[' + str(choice1) + ']/input'
        username = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[3]')
        password = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[4]')
        isp = driver.find_element_by_xpath(ispchoice)
        submit = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[2]')
    except Exception:
        pass
    finally:
        username.send_keys(user)
        password.send_keys(pwd)
        isp.click()
        submit.click()
    Ping()

# 测试网络连通性
def Ping():
    time.sleep(TIME)
    global m
    try:
        p = requests.get('http://www.baidu.com')
        pattern = r"172\.21\.255\.105"
        m = re.search(pattern, p.url)
    except Exception:
        pass
    finally:
        if m:
            print('连接失败,正在重试...')
            Connect()
        else:
            print('连接成功!')
            driver.close()


if __name__ == "__main__":
    Check()
   
