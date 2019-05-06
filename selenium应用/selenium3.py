from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_argument('--headless')
driver= webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()

choice1 = input('请输入网络服务运行商(1.移动 2.电信 3.联通 4.校园网):')
choice1 = int(choice1) + 1
ispchoice = '//*[@id="edit_body"]/div[2]/div[2]/div/span['+str(choice1) + ']/input'
user = input('请输入用户名:')
pwd = input('请输入密码:')
driver.get("http://172.21.255.105/a79.htm?userip=172.22.172.146&wlanacname=&wlanacip=172.21.255.106&usermac=e4939d93a054e93282e0b5d3f7aef7ce0ca1f353faaee02a")
username = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[3]')
password = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[4]')
isp = driver.find_element_by_xpath(ispchoice)
submit = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/form/input[2]')
username.send_keys(user)
password.send_keys(pwd)
isp.click()
submit.click()
