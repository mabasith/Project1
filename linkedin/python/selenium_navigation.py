#!/usr/bin/env python3
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.selenium.dev')

element = driver.find_element_by_xpath('/html/body/header/nav/a[1]')
element.click()

driver.back()

search_element = driver.find_element_by_id('gsc-i-id1')
search_element.send_keys('webdriver')

go_button = driver.find_element_by_xpath('/html/body/header/nav/div[2]/div/img')
go_button.click()