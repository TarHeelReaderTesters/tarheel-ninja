from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
import time

MAX_WAIT_TIME=30

class AmazonExplorer:
    def __init__(self):
        usingChrome=False
        
        #Too many input arguments?
        if(len(sys.argv)>2):
            print "Incorrect number of parameters!"
            print "Format is: %s [-c]" % (sys.argv[0],)
            sys.exit(1)
        elif(len(sys.argv)==2 and sys.argv[1]=="-c"):
            usingChrome=True
        
        #Figure out what browser we are going to use
        if(usingChrome):
            chromedriver = "/Users/huynhl/selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self._browser = webdriver.Chrome(chromedriver)
        else:
            self._browser=webdriver.Firefox()
        
        self.explore_amazon()
    
    def explore_amazon(self):
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
            print("Can't find amazon link!")
            self.close_browser(1)
        
        #Types in 'creeper' into search box on amazon.com homepage
        try:
            searchBox=self._browser.find_element_by_id("twotabsearchtextbox")
            searchBox.send_keys("creeper"+Keys.RETURN)
        
        except NoSuchElementException:
            print("Can't find amazon search box!")
            self.close_browser(1)
        
        #Looks for the 'Creeper Plush' toy in the amazon search results
        try:
            creeperPlushLink=self._browser.find_element_by_partial_link_text("Minecraft: Creeper Plush")
            creeperPlushLink.click()
        
        except NoSuchElementException:
            print("Can't find creeper plush link!")
            self.close_browser(1)
        
        #Tries to actually add the 'Creeper Plush' toy to our shopping cart
        try:
            addToCartButton=self._browser.find_element_by_xpath("//input[@id='bb_atc_button' or @id='add-to-cart-button']")
            addToCartButton.click()
        
        except NoSuchElementException:
            print("Can't find \'Add to Cart\' button!")
            self.close_browser(1)
        
        self.close_browser(0)
    
    def close_browser(self, exit_code):
        """Closes the browser when the program exits
            exit_code--what value the program is exiting with
            (depends on whether or not an error occurred)
            """
        time.sleep(5.0)
        self._browser.close()
        sys.exit(exit_code)

#Starts the program
if __name__ == '__main__':
    AmazonExplorer()
    sys.exit(0)