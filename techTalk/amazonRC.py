from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
import time
import unittest

MAX_WAIT_TIME=30

class AmazonRC(unittest.TestCase):
    def setUp(self):
        if(param == 3):
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[0],"browserName": param[1], "version": param[2]})
            print param
        else:
            self._browser = webdriver.Remote(desired_capabilities = {"platform": param[0],"browserName": param[1]})
            print param

    def test_AmazonRC(self):
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
            exit_code--what value the program is exiting with
            (depends on whether or not an error occurred)
            """
        time.sleep(5.0)
        print param
        self._browser.close()

#Starts the program
if __name__ == '__main__':
    param = []
    if len(sys.argv) == 4:
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        param.append(sys.argv[3])
        del sys.argv[1:]
        del sys.argv[2:]
        del sys.argv[3:]
    else:
        param.append(sys.argv[1])
        param.append(sys.argv[2])
        del sys.argv[1:]
        del sys.argv[2:]

    unittest.main()