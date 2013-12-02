from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30
NUMBER_OF_PAGES=9
usingChrome=False

class BackButtonTester(unittest.TestCase):
	def setUp(self):
		if len(param) == 4:
			self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2], "version": param[3]})
		else:
			self._browser = webdriver.Remote(desired_capabilities = {"platform": param[1],"browserName": param[2]})
		
	def test_back_button(self):
		"""Runs the back button test for Tar Heel Reader
		"""

		self._browser.get("http://tarheelreader.org/2010/08/26/i-like-sonic-cartoons/9/")
		self._browser.implicitly_wait(MAX_WAIT_TIME)

		#Read one page at a time of current book
		for i in range(0, NUMBER_OF_PAGES):
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
        if len(param) == 4:
            print '\nTest: ' + param[0]
            print 'Platform: ' + param[1]
            print 'Browser: ' + param[2]
            print 'Version: ' + param[3]
        else:
            print len(param)
            print '\nTest: ' + param[0]
            print 'Platform: ' + param[1]
            print 'Browser: ' + param[2]
        self._browser.quit()

if __name__=='__main__':
	param = []
    if len(sys.argv) == 4:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        del sys.argv[1:]

    else:
        param.append(sys.argv[0])
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        del sys.argv[1:]
	unittest.main()
