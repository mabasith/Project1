#!/usr/bin/env python3
from selenium import webdriver

driver =webdriver.Chrome()

driver.get('http://www.phptravels.net/offers')

a_tags = driver.find_elements_by_tag_name('a')

price_list = []

for a in a_tags:
    price_list.append(a.text)

print(price_list)


