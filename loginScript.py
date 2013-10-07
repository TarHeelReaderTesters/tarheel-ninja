from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import traceback

MAX_WAIT_TIME=30

class LoginAutomator:
	def __init__(self):
		#Do we have right number of parameters?
                if(len(sys.argv)!=3):
			print "Incorrect number of parameters!"
			print "Format is: %s <username> <password>" % (sys.argv[0],)
			sys.exit(1)

		chromedriver = "/home/dallara/SeleniumDrivers/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self._browser=webdriver.Chrome(chromedriver)
		self.run_test()

	def run_test(self):
		"""Runs the login test for Tar Heel Reader
		"""

		self._browser.get("http://tarheelreader.org") # Load tar heel reader
		assert "Tar Heel Reader" in self._browser.title

		#Click "Write Book" button so we will be taken to login page
		try:
    			writeButton=self._browser.find_element_by_xpath("//a[contains(@href,'/write/')]")
    			writeButton.click()
		except NoSuchElementException:
    			assert 0, "can't find write book button"

		#Click login button
		self._browser.implicitly_wait(MAX_WAIT_TIME)
		try:
    			loginButton=self._browser.find_element_by_xpath("//a[contains(@href,'/login/?goto=write')]")
    			loginButton.click()
		except NoSuchElementException:
    			assert 0, "can't find login button"

		#Try to login with input username/password pair
		self._browser.implicitly_wait(MAX_WAIT_TIME)
		try:
    			usernameField=self._browser.find_element_by_xpath("//input[@name='log']")
    			passwordField=self._browser.find_element_by_xpath("//input[@name='pwd']")
    			loginButton=self._browser.find_element_by_xpath("//input[@name='wp-submit']")
    			usernameField.send_keys(str(sys.argv[1]))
    			passwordField.send_keys(str(sys.argv[2]))
    			loginButton.click()
		except NoSuchElementException:
    			traceback.print_exc()

		#Close browser
		time.sleep(3.0)
		self._browser.close()

if __name__=='__main__':
	loginAutomator=LoginAutomator()
	sys.exit(0)
