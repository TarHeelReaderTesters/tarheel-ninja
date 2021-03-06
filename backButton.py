from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30



class BackButtonTester(unittest.TestCase):
	def setUp(self):
    	#checks if command contains a browser version
        	self.url = param[1]
        	if len(param) == 5:
            		self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3], "version": param[4]})
        	else:
            		self._browser = webdriver.Remote(desired_capabilities = {"platform": param[2],"browserName": param[3]})
                    
            	if param[1] == "http://gbserver3.cs.unc.edu":
                	self._book = "http://gbserver3.cs.unc.edu/2011/02/28/mice-like-to-play-and-hide/6/"
                   	self._numPages = 5
            	else:
                	self._book= "http://tarheelreader.org/2013/11/18/tarheelreadertestbook/5/"
                    	self._numPages = 6
		
	def test_back_button(self):
		"""Runs the back button test for Tar Heel Reader
		"""

		self._browser.get(self._book)
		self._browser.implicitly_wait(MAX_WAIT_TIME)

		#Read one page at a time of current book
		for i in range(0, self._numPages):
			try:
				time.sleep(3.0)

				previousPageLink=self._browser.find_element_by_link_text("Back")
				previousPageLink.click()

			except NoSuchElementException:
				assert 0, "could not find 'Back' button!"

	def tearDown(self):
		"""Closes the browser when the program exits
		"""
        	time.sleep(5.0)
        	#formats output with browser version
        	if len(param) == 5:
            		print '\nTest: ' + param[0]
            		print 'URL: ' + param[1]
            		print 'Platform: ' + param[2]
            		print 'Browser: ' + param[3]
            		print 'Version: ' + param[4]
        
       		else:
       		#formats output without browser version
            		print '\nTest: ' + param[0]
            		print 'URL: ' + param[1]
            		print 'Platform: ' + param[2]
            		print 'Browser: ' + param[3]
        	self._browser.quit()


if __name__=='__main__':
	#python Unittest requires an empty array.  So save the current paramters, then delete them.
    param = []
    if len(sys.argv) == 5:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        param.append(sys.argv[4])
        del sys.argv[1:]
    else:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        del sys.argv[1:]
    
    unittest.main()
