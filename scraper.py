import sys
import getpass
import requests
import time
from selenium import webdriver

print("Enter instagram username and password");
(username, password) = (sys.stdin.readline().rstrip(), getpass.getpass())

# Authenticate
driver = webdriver.Chrome()
driver.get("http://www.instagram.com")
assert "Instagram" in driver.title

time.sleep(3)

el_username = driver.find_element_by_name("username")
el_username.clear()
el_username.send_keys(username)

el_password = driver.find_element_by_name("password")
el_password.clear()
el_password.send_keys(password)

el_form = driver.find_element_by_css_selector("main form")

el_form.submit()

# driver.close()