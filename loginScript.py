from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import traceback

#Do we have right number of parameters?
if(len(sys.argv)!=3):
    print "Incorrect number of parameters!"
    print "Format is: loginScript.py <username> <password>"
    sys.exit(1)

chromedriver = "/home/dallara/SeleniumDrivers/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

# Create a new instance of the Chrome driver
browser = webdriver.Chrome(chromedriver) # Get local session of chrome
browser.get("http://tarheelreader.org") # Load tar heel reader
assert "Tar Heel Reader" in browser.title

#Click "Write Book" button so we will be taken to login page
time.sleep(2.0)
try:
    writeButton=browser.find_element_by_xpath("//a[contains(@href,'/write/')]")
    writeButton.click()
except NoSuchElementException:
    assert 0, "can't find write book button"

#Click login button
time.sleep(2.0)
try:
    loginButton=browser.find_element_by_xpath("//a[contains(@href,'/login/?goto=write')]")
    loginButton.click()
except NoSuchElementException:
    assert 0, "can't find login button"

#Try to login with known username/password pair
time.sleep(2.0)
try:
    usernameField=browser.find_element_by_xpath("//input[@name='log']")
    passwordField=browser.find_element_by_xpath("//input[@name='pwd']")
    loginButton=browser.find_element_by_xpath("//input[@name='wp-submit']")
    usernameField.send_keys(str(sys.argv[1]))
    passwordField.send_keys(str(sys.argv[2]))
    loginButton.click()
except NoSuchElementException:
    traceback.print_exc()

time.sleep(5.0)
browser.close()
