from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json

def login():
	driver = webdriver.Firefox()
	#specify the url to hit for autologin
	driver.get("http://172.16.68.6:8090/httpclient.html")
	inputEmail = driver.find_elements_by_class_name("textbox")
	#specify USERNAME and PASSWORD
	inputEmail[0].send_keys("12503853")
	inputEmail[1].send_keys("abheetkg")
	
	inputEmail[1].submit()
	
	msg1=[]
	msg2=[]
	try:
		msg1.append(driver.find_element_by_class_name("errorfont"))
	except:
		pass
	try:	
		msg2.append(driver.find_element_by_class_name("note"))
	except:
		pass
	
	if not msg1:
		print msg2[0].text.encode("utf-8")
	else:
		print msg1[0].text.encode("utf-8")
	
	
	driver.close()
if __name__ == '__main__':
	login()





