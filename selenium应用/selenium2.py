import requests
from selenium import webdriver
 
driver= webdriver.Chrome()
driver.maximize_window()

driver.get("http://study.lanwang.online/login.html")
name = driver.find_element_by_name('username')
name.send_keys('1353433900')
password = driver.find_element_by_name('password')
password.send_keys('aa88700420')
# driver.quit()
driver.find_element_by_name('submit').click()
