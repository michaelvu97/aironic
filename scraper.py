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

time.sleep(3)

instagram_accounts_list = [ 
	"jokers_quotes_"
]

for account_id in instagram_accounts_list:
	driver.get("https://www.instagram.com/" + account_id)
	el_images = driver.find_elements_by_css_selector("article img[src]")

	for el_image in el_images:
		print(el_image.get_attribute("src"))

	# driver.close()