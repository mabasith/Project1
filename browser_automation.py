# # from selenium import webdriver
# # browser=webdriver.Firefox('/home/hitech/Downloads')
# # browser.get('https://www.seleniumhq.org')
# # elem=browser.find_element_by_link_text('Download')
# # elem.click()
# # search=browser.find_element_by_id('q')
# # search.send_keys('Download')
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By 
# import time
# driver=webdriver.Firefox('/home/hitech/.local/bin')
# driver.get('https://web.whatsapp.com/')
# wait=WebDriverWait(driver,600)
# target='"Sabith"'
# string='assalamu alaikum!!'
# x_arg='//span[contains(@title, '+ target + ')]'

# target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))

# target.click()
# input_box=driver.find_element_by_class_name('_13mgZ')
# for i in range(50):
# 	input_box.send_keys(string+Keys.ENTER)
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Firefox('/home/hitech/.local/bin') 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Uppa Home"'

# Replace the below string with your own message 
string = "Message sent using Python!!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
group_title.click() 
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 
for i in range(100): 
	input_box.send_keys(string + Keys.ENTER) 
	time.sleep(1) 