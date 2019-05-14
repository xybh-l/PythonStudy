from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# # chrome_options.add_argument('--headless')
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("http://172.21.255.105/")

def up():
    choice = input('1.自动登录 2.手动登录:')
    x=1
    global choice1
    global user
    global pwd
    while x==1:
        if choice == '1':
            user = 201820180113
            pwd = 888999
            choice1 = '2'
            x=0
        elif choice == '2':
            choice1 = input('请输入网络服务运行商(1.移动 2.电信 3.联通 4.校园网):')
            choice1 = int(choice1) + 1
            user = input('请输入用户名:')
            pwd = input('请输入密码:')
            x=0
        else:
            choice = input('请重新输入:')
            x=1

def connect():
    global choice1,pwd,user
    try:
        loginable = []
        loginable = driver.get('//*[@id="edit_body"]/div[1]/div[1]/form/input').text
        print(loginable)
    except Exception as i:
        pass
    finally:
        if loginable == '注  销':
            driver.quit()
            print("你已登录!")
            exit()
    try:
        message = driver.get('//*[@id="message"]').text
    except Exception as id:
        pass
    else:
        print("密码错误!")
    ispchoice = '//*[@id="edit_body"]/div[2]/div[2]/div/span['+str(choice1) + ']/input'
    username = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[3]')
    password = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[4]')
    isp = driver.find_element_by_xpath(ispchoice)
    submit = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[2]')
    username.send_keys(user)
    password.send_keys(pwd)
    isp.click()
    submit.click()
    ping()

def ping():
    p = requests.get('http://www.baidu.com')
    if p.status_code==200:
        print('连接成功!')
    else:
        print('连接失败,正在重试...')
        connect()

if __name__ == "__main__":
    up()
    connect()