#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

url = 'http://automationpractice.com/index.php?id_category=3&cont'
driver.get(url)

product_containers = driver.find_elements_by_class_name('product-container')

for index,product_container in enumerate(product_containers):
    hover = ActionChains(driver).move_to_element(product_container)
    hover.perform()
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1)).click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/span/span').click()
    time.sleep(0.5)





