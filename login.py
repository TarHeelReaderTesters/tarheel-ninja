from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import traceback
import unittest

MAX_WAIT_TIME=30
username = ""
password = ""

class login(unittest.TestCase):
    def setUp(self):
        if len(param) == 6:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[3],"browserName": param[4], "version": param[5]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[3],"browserName": param[4]})
        username = param[1]
        password = param[2]

    def test_login(self):
	"""Runs the login test for Tar Heel Reader """
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
        if len(param) == 4:
            print '\nTest: ' + param[0]
            print 'Platform: ' + param[3]
            print 'Browser: ' + param[4]
            print 'Version: ' + param[5]
        else:
            print len(param)
            print '\nTest: ' + param[0]
            print 'Platform: ' + param[3]
            print 'Browser: ' + param[4]
		self._browser.quit()

if __name__=='__main__':
    param = []
    if len(sys.argv) == 6:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        param.append(sys.argv[4])
        param.append(sys.argv[5])
        del sys.argv[1:]
    else:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        param.append(sys.argv[4])
        del sys.argv[1:]
    print param
    unittest.main()
