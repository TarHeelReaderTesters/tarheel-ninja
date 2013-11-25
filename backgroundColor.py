import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time
import re


#testing background colors


browser = webdriver.Firefox()
browser.get('http://tarheelreader.org/2013/10/22/pandas-can-eat/')
browser.implicitly_wait(2)

settings = browser.find_element_by_xpath("//img[contains(@src,'/themeV1/images/settings.png')]")# Find the settings menu
settings.click()
colors = browser.find_element_by_xpath("//span[contains(@class,'colors')]")# Find the Colors menu
colors.click()
pageColor = browser.find_element_by_xpath("//span[contains(text(),'Page Color')]")# Find the Page Color menu
pageColor.click()
colorSelect = browser.find_element_by_xpath("//span[contains(@class,'magenta')]")# choose a color
colorSelect.click()


rgb = browser.find_element_by_xpath("//div[contains(@class,'thr-book-page')]").value_of_css_property('background-color')
browser.quit()
print rgb
if rgb == "rgba(255, 0, 255, 1)":
        print "background color values are equal"

else:
    print "background color values are not equal"



