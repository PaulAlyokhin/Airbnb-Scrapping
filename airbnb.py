from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv
import collections

homeid = '770561 Houstonian, Houston, TX'
checkin = '11/01/2018'
checkout = '12/31/2018'

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\dell\AppData\Local\Google\Chrome\Application\chrome.exe"
chrome_driver_path = r"chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
driver.get("https://www.airbnb.com/")
elem = driver.find_element_by_id("Koan-magic-carpet-koan-search-bar__input")
elem.send_keys(homeid)
driver.execute_script("document.getElementById('checkin_input').setAttribute('value', '11/01/2018')")
driver.execute_script("document.getElementById('checkout_input').setAttribute('value', '12/31/2018')")
#elem = driver.find_element_by_id("checkin_input")
#elem.send_keys(checkin)
#elem = driver.find_element_by_id("checkout_input")
#elem.send_keys(checkout)
elem = driver.find_element_by_xpath('//*[@id="lp-search-button"]/div/button')
elem.submit()
page = driver.page_source

soup = BeautifulSoup(page, "html.parser")
source = soup.select('#site-content > div > div > div > div > div > div > div > div > div > div > div > div > div > div > div')#listing-1048435 > div._v72lrv > a > div._wuffzwa > div > small#listing-1048435 > div._v72lrv > a > div:nth-child(2) > div > div#listing-1048435 > div._v72lrv > a > div:nth-child(3) > div > div._ncmdki > div > span > span > span#listing-1048435 > div._v72lrv > a > div:nth-child(3) > div > div._y9ev9r > div > span._17oldnte#listing-1048435 > div._v72lrv > a > div:nth-child(4) > div > div > span._1gvnvab > span#listing-1048435 > div._v72lrv > a > div:nth-child(4) > div > span·
writer = csv.writer(open("test.csv", "w"))
text = []
entries = []
for element in source:
	text.append(element.text)
	entries = element.text.split("·")
	writer.writerows(entries)
	print(element.text)
writer.close()
