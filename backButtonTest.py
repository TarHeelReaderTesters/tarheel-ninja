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
                #Figure out what browser we are going to use
                if(usingChrome):
                        chromedriver = "/home/dallara/SeleniumDrivers/chromedriver"
                        os.environ["webdriver.chrome.driver"] = chromedriver
                        self._browser = webdriver.Chrome(chromedriver)
                else:
                        self._browser=webdriver.Firefox()

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
		self._browser.quit()

if __name__=='__main__':
	if(len(sys.argv)>2): #Too many or incorrect input arguments?
        	print "Incorrect number of parameters!"
                print "Format is: %s [-c]" % (sys.argv[0],)
		sys.exit(1)
        elif(len(sys.argv)==2):
                if(sys.argv[1]=="-c"):
                	usingChrome=True
                else:
                        print "Error in '%s' parameter!" % (sys.argv[1],)
                        print "Format is: %s [-c]" % (sys.argv[0],)
			sys.exit(1)

	del sys.argv[1:]
	unittest.main()
