from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import traceback
import unittest

MAX_WAIT_TIME=30

class login(unittest.TestCase):
    def setUp(self):
        if len(param) == 7:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[4],"browserName": param[5], "version": param[6]})
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[4],"browserName": param[5]})
        self.url = param[1]
        self.username = param[2]
        self.password = param[3]
        
    def is_present(self):
    #checks if server supports logging in, a message will appear on the login screen if logging in is not supported
        try:
            message = self._browser.find_element_by_xpath("//p[@class='message']")
        except NoSuchElementException, e:
            return False

    def test_login(self):
	#Runs the login test for Tar Heel Reader
        self._browser.get(self.url + '/login') # Load tar heel reader
        assert "Tar Heel Reader" in self._browser.title
        
	self._browser.implicitly_wait(MAX_WAIT_TIME)
	#Click "Write Book" button so we will be taken to login page
    
        #Try to login with input username/password pair
        try:
            time.sleep(5.0)
            usernameField=self._browser.find_element_by_xpath("//input[@name='log']")
            passwordField=self._browser.find_element_by_xpath("//input[@name='pwd']")
            loginButton=self._browser.find_element_by_xpath("//input[@name='wp-submit']")
            usernameField.send_keys(self.username)
            passwordField.send_keys(self.password)
            loginButton.click()
            
            if self.is_present() == False:
                print ""
            else:
                print "Login Failed"

        
        except NoSuchElementException:
            assert 0, "Unable to login"


    def tearDown(self):
        #Closes the browser when the program exits
        
        time.sleep(5.0)
        if len(param) == 7:
            print '\nTest: ' + param[0]
            print 'Url: ' + param[1]
            print 'Platform: ' + param[4]
            print 'Browser: ' + param[5]
            print 'Version: ' + param[6]
        else:
            print '\nTest: ' + param[0]
            print 'Url: ' + param[1]
            print 'Platform: ' + param[4]
            print 'Browser: ' + param[5]
        self._browser.quit()

if __name__ == '__main__':
    param = []
    if len(sys.argv) == 7:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        param.append(sys.argv[4])
        param.append(sys.argv[5])
        param.append(sys.argv[6])
        del sys.argv[1:]
    else:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        param.append(sys.argv[4])
        param.append(sys.argv[5])
        del sys.argv[1:]
    unittest.main()
