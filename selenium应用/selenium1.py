import requests
from selenium import webdriver
 
driver= webdriver.Chrome()
driver.maximize_window()
 
# driver.get("http://www.santostang.com/2018/07/04/hello-world/")
driver.get("http://study.lanwang.online/regist.html")
name = driver.find_element_by_name('username')
name.send_keys('1353433900')
password = driver.find_element_by_name('password')
password.send_keys('aa88700420')
confirm = driver.find_element_by_name('confirm')
confirm.send_keys('aa88700420')
phone = driver.find_element_by_name('phone')
phone.send_keys('17687974147')
check = driver.find_element_by_name('check_box')
check.send_keys('17687974147')
driver.find_element_by_class_name('submit_button').click()
