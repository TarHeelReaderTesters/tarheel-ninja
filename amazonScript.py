from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30
usingChrome=False

class AmazonExplorer(unittest.TestCase):
	def setUp(self):
        	#Figure out what browser we are going to use
        	if(usingChrome):
        		chromedriver = "/home/dallara/SeleniumDrivers/chromedriver"
        		os.environ["webdriver.chrome.driver"] = chromedriver
        		self._browser = webdriver.Chrome(chromedriver)
        	else:
        		self._browser=webdriver.Firefox()

	def test_amazon_exploration(self):
		"""Goes to amazon.com, looks for a minecraft creeper toy,
		   and adds it to the shopping cart
		"""

		self._browser.get("https://www.google.com")
		self._browser.implicitly_wait(MAX_WAIT_TIME)

		#Searches for amazon.com website through google
		google_search_field=self._browser.find_element_by_name("q")
		google_search_field.send_keys("amazon"+Keys.RETURN)

		#Single out link to amazon.com in search results
		try:
			amazonLink=self._browser.find_element_by_partial_link_text("Amazon.com")
			amazonLink.click()

		except NoSuchElementException:
			assert 0, "Can't find amazon link!"

		#Types in 'creeper' into search box on amazon.com homepage
		try:
			searchBox=self._browser.find_element_by_id("twotabsearchtextbox")
			searchBox.send_keys("creeper"+Keys.RETURN)

		except NoSuchElementException:
			assert 0, "Can't find amazon search box!"

		#Looks for the 'Creeper Plush' toy in the amazon search results
		try:
			creeperPlushLink=self._browser.find_element_by_partial_link_text("Minecraft: Creeper Plush")
			creeperPlushLink.click()

		except NoSuchElementException:
			assert 0, "Can't find creeper plush link!"

		#Tries to actually add the 'Creeper Plush' toy to our shopping cart
		try:
			addToCartButton=self._browser.find_element_by_xpath("//input[@id='bb_atc_button' or @id='add-to-cart-button']")
			addToCartButton.click()

		except NoSuchElementException:
			assert 0, "Can't find \'Add to Cart\' button!"

	def tearDown(self):
		"""Closes the browser when the program exits
		"""
		time.sleep(5.0)
		self._browser.quit()

#Starts the program
if __name__ == '__main__':
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
