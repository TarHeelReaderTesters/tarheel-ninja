from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import traceback
import unittest

MAX_WAIT_TIME=30

usingChrome=False
username=""
password=""

class LoginAutomator(unittest.TestCase):
	def setUp(self):
		#Figure out what browser we are going to use
		if(usingChrome):
			chromedriver = "/home/dallara/SeleniumDrivers/chromedriver"
			os.environ["webdriver.chrome.driver"] = chromedriver
			self._browser=webdriver.Chrome(chromedriver)
		else:
			self._browser=webdriver.Firefox()

	def test_login(self):
		"""Runs the login test for Tar Heel Reader
		"""

		self._browser.get("http://tarheelreader.org") # Load tar heel reader
		assert "Tar Heel Reader" in self._browser.title

		self._browser.implicitly_wait(MAX_WAIT_TIME)

		#Click "Write Book" button so we will be taken to login page
		try:
    			writeButton=self._browser.find_element_by_xpath("//a[contains(@href,'/write/')]")
    			writeButton.click()
		except NoSuchElementException:
    			assert 0, "can't find write book button"

		#Click login button
		try:
    			loginButton=self._browser.find_element_by_xpath("//a[contains(@href,'/login/?goto=write')]")
    			loginButton.click()
		except NoSuchElementException:
    			assert 0, "can't find login button"

		#Try to login with input username/password pair
		try:
    			usernameField=self._browser.find_element_by_xpath("//input[@name='log']")
    			passwordField=self._browser.find_element_by_xpath("//input[@name='pwd']")
    			loginButton=self._browser.find_element_by_xpath("//input[@name='wp-submit']")
    			usernameField.send_keys(username)
    			passwordField.send_keys(password)
    			loginButton.click()
		except NoSuchElementException:
    			assert 0, str(traceback.print_exc())

	def tearDown(self):
		"""Closes the browser when the program exits
		"""

		time.sleep(5.0)
		self._browser.quit()

if __name__=='__main__':
	usingChrome=False

	#Do we have right number of parameters?
        if(len(sys.argv)<3 or len(sys.argv)>4):
                print "Incorrect number of parameters!"
                print "Format is: %s <username> <password> [-c]" % (sys.argv[0],)
                sys.exit(1)
        elif(len(sys.argv)==4):
                if(sys.argv[3]=="-c"):
                        usingChrome=True
                else:
                        print "Error in '%s' parameter!" % (sys.argv[3],)
                        print "Format is: %s <username> <password> [-c]" % (sys.argv[0],)
                        sys.exit(1)

	username=str(sys.argv[1])
	password=str(sys.argv[2])

	del sys.argv[1:] #Eliminate command line arguments so that unittest doesn't reinterpret them
	unittest.main()
